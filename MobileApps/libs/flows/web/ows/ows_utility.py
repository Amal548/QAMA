import json
import base64
import logging
import requests
from MobileApps.libs.ma_misc import ma_misc

PROFILES = {
    'limo': {'modelName': 'HP'},
    'palermo': {'modelName': 'HP Envy 7100 All-in-One Printer'},
    'ellis': {'modelName': 'HP'},
    'verona': {'modelName': 'HP Envy 5030'},
    'palermolow': {'modelName': 'HP Envy 7100 All-in-One Printer'},
    'palermolowder1': {'modelName': 'HP Envy 7100 All-in-One Printer'},
    'infinitybaseder2': {'modelName': 'HP TANGO'},
    'skyreach': {'modelName': 'HP LaserJet MFP'},
}
SERVER_STACKS = {
    'pie': {
        'dcs_base_uri': 'https://deviceclaim.pie.avatar.ext.hp.com/dcs-api'
    },
    'stage': {
        'dcs_base_uri': 'https://deviceclaim.stage.avatar.ext.hp.com/dcs-api',
    },
}
PROXIES = {
    'http': 'http://web-proxy.corp.hp.com:8080',
    'https': 'http://web-proxy.corp.hp.com:8080',
}

def create_simulated_gen2_printer(stack='pie', profile='skyreach', offer=0, include_postcard=True, biz_model='E2E',
                                  include_fingerprint=True):
    # https://rndwiki.corp.hpicorp.net/confluence/pages/viewpage.action?title=Printer+Simulator+APIs&spaceKey=IWSWebPlatform
    # Supported Stacks
    #    pie
    #    stage
    # Supported Profiles
    # | profile          | model number |
    # +------------------+--------------+
    # | limo             | A7W94A       |
    # | palermo          | K7R96A       |
    # | ellis            | Y0S19A       |
    # | verona           | M2U75A       |
    # | palermolow       | K7G18A       |
    # | palermolowder1   | K7G93A       |
    # | infinitybaseder2 | 2RY54A       |
    # | skyreach         | 6GX01A       |

    printer_data = {}
    sim_base_uri = 'https://g2sim.wpp.api.hp.com'
    create_payload = {"stack": stack,
                      "profile": profile,
                      "biz_model": biz_model,
                      "offer": offer
                      }
    if profile in ['skyreach', 'manhattan_yeti']:
        create_payload.update({"fipsflag": "true"})
    # create printer
    headers = {'Content-Type': 'application/json'}
    resp = requests.post('{}/wpp/simulator/printers'.format(sim_base_uri),
                         headers=headers,
                         data=json.dumps(create_payload),
                         verify=False,
                         proxies=PROXIES)

    if resp.status_code != 201:
        raise Exception('Create printer - Failed: {}{}'.format(resp.status_code, resp.text))
    logging.debug("Create printer - Success")
    body = resp.json()
    serial_number = body['entity_id']
    uuid = body['uuid']
    printer_data['serial_number'] = serial_number
    printer_data['uuid'] = uuid
    printer_data['model_number'] = body['model_number']
    # register printer
    logging.debug("Register printer - Started")
    resp = requests.post('{}/wpp/simulator/printers/{}/register'.format(sim_base_uri, serial_number),
                         headers=headers,
                         verify=False,
                         proxies=PROXIES)
    if resp.status_code != 200:
        raise Exception('Register printer - Failed: {}'.format(resp.status_code))
    logging.debug("Register printer - Success")
    # create claimPostcard
    if include_postcard:
        logging.debug("Create claimPostcard - Started")
        resp = requests.post('{}/wpp/simulator/printers/{}/claimpostcard'.format(sim_base_uri, serial_number),
                             headers=headers,
                             verify=False,
                             proxies=PROXIES)
        if resp.status_code != 200:
            raise Exception('Create claimPostcard - Failed: {}'.format(resp.status_code))

        logging.debug("Create claimPostcard - Success")
        printer_data['claim_postcard'] = resp.content.decode("utf-8")

    # get fingerprint
    if include_fingerprint:
        logging.debug("Get fingerprint - Started")
        resp = requests.get('{}/wpp/simulator/printers/{}/devicefingerprint'.format(sim_base_uri, serial_number),
                            headers=headers,
                            verify=False,
                            proxies=PROXIES)
        if resp.status_code != 200:
            raise Exception('Get fingerprint - Failed: {}'.format(resp.status_code))

        logging.debug("Get fingerprint - Success")
        fingerprint = resp.content
        printer_data['fingerprint'] = fingerprint.decode("utf-8")
    return printer_data

def load_product_config_dyn(product, uuid):
    file_path = ma_misc.get_abs_path("resources/test_data/ows/" + product + "_pcd.xml")
    fh = open(file_path)
    xml = fh.read()
    fh.close()
    return base64.b64encode(xml.format(uuid).encode("utf-8")).decode("utf-8")

def patch_credential(url, payload):
    resp = requests.patch(url, json=payload)
    if resp.status_code != 204:
        raise Exception('Patch credential - Failed: {}'.format(resp.status_code))
    else:
        return True