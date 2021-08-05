#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Test_Suite_03_OOBE_No_Beaconing

@author: ten
@create_date: Aug 6, 2019
'''
import logging
import pytest

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.flows import flows_oobe

# REQUIRED
pytest.app_info = "SMART"


class Test_Suite_03_OOBE_No_Beaconing(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.flows_oobe = flows_oobe.OOBEFlows(self.driver)
        self.printer_type = smart_const.OWS_TYPE.PALERMO_GEN2_INKJET

    def test_01_go_through_agreement_screen(self):
        '''
        go through agreement
        '''
        logging.debug("go through agreement...")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_inital_screen()

    def test_02_start_oobe_flow_no_beaconing(self):
        '''
        go through oobe flow with no printer beaconing
        '''
        logging.debug("go through oobe flow with no printer beaconing...")
        self.flows_oobe.go_through_oobe_flow_no_beaconing()

    def test_03_go_through_ows_flow(self):
        '''
        Go through OWS workflow
        '''
        logging.debug("Go through OWS workflow")
        self.flows_oobe.go_through_ows_flow()

    def test_04_go_to_main_ui(self):
        '''
        Go to main_ui with printer added
        '''
        logging.debug("Go to main_ui with printer added")
        self.flows_oobe.after_ows_to_main_ui_flow()


