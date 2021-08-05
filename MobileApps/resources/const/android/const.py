import os
from MobileApps.libs.ma_misc import ma_misc

#trail 1

class NONE_THIRD_PARTY_APP():
    APP_LIST = ["HPPS", "SMART", "JWEB", "JWEB_DATA_COLLECTION"]

class FILE_LIST():
    PDF = ["10pages.pdf", "10pages_20mb.pdf", "1page.pdf", "1page_1mb.pdf", "1page_3mb.pdf",
           "2pages.pdf", "2pages_20mb.pdf", "3Pagepdf.pdf", "3pages.pdf", "4page_12mb.pdf",
           "4pages.pdf", "8Pagepdf.pdf"]
class WEBVIEW_CONTEXT():
    SMART = 'WEBVIEW_com.hp.printercontrol.debug'
    JWEB = 'WEBVIEW_com.hp.jwebreference'
    CHROME = 'WEBVIEW_chrome'

class WEBVIEW_URL():
    HPID = "https://login3.stg.cd.id.hp.com"
    SMART_WELCOME = "in-app/android"
    OWS_VALUE_PROP = "ucde/account-prop/"
    UCDE_PRIVACY = "ucde/terms-conditions"
    SOFTFAX_OFFER = "in-app/mobile-fax"
    SOFTFAX = "sws"
    HP_CONNECT = "/ucde"
    HP_CONNECT_BASIC_ACCOUNT = "/newprinter"
    PRINTER_CONSENT = "/printer-consents"

class PACKAGE():
    SMART = {"debuggable": "com.hp.printercontrol", "default": "com.hp.printercontrol.debug"}
    HPPS = "com.hp.android.printservice"
    SETTINGS = "com.android.settings"
    GOOGLE_DRIVE = 'com.google.android.apps.docs'
    GOOGLE_PHOTOS = 'com.google.android.apps.photos'
    SAMSUNG_GALLERY = "com.sec.android.gallery3d"
    GOOGLE_DOCS = "com.google.android.apps.docs.editors.docs"
    GOOGLE_SHEETS = 'com.google.android.apps.docs.editors.sheets'
    WPS_OFFICE = 'cn.wps.moffice_eng'
    GOOGLE_SLIDES = 'com.google.android.apps.docs.editors.slides'
    ADOBE = 'com.adobe.reader'
    MORELANGS = 'sightidea.com.setlocale'
    GOOGLE_CHROME = 'com.android.chrome'
    WPRINT_TEST = "com.hp.droid.wprinttestapp"
    DROPBOX = "com.dropbox.android"
    GMAIL = "com.google.android.gm"
    MICROSOFT_WORD = "com.microsoft.office.word"
    FACEBOOK = "com.facebook.katana"
    WPRINT_DEBUG = "com.hp.wprint.debug.enabler"
    HPBRIDGE = "com.tencent.mm"
    HPPS = 'com.hp.android.printservice'
    GOOGLE_PLAY = 'com.android.vending'
    MICROSOFT_EXCEL = 'com.microsoft.office.excel'
    JWEB = 'com.hp.jwebreference'
    JWEB_DATA_COLLECTION = 'com.hp.jarvis.datacollectionexample'

class LAUNCH_ACTIVITY():
    HPPS = '.launcher.WelcomeActivity'
    SMART = "com.hp.printercontrol.base.PrinterControlActivity"
    SMART_DEV_SETTINGS = "com.hp.sdd.common.library.internal.testing.ActivityDevSettingsList"
    SETTINGS = "com.android.settings.Settings"
    GOOGLE_DRIVE = 'com.google.android.apps.docs.app.NewMainProxyActivity'
    GOOGLE_PHOTOS = '.home.HomeActivity'
    SAMSUNG_GALLERY = "com.android.gallery3d.app.Gallery"
    GOOGLE_DOCS =  'com.google.android.apps.docs.app.NewMainProxyActivity'
    GOOGLE_SHEETS = 'com.google.android.apps.docs.app.NewMainProxyActivity'
    WPS_OFFICE = 'cn.wps.moffice.main.StartPublicActivity'
    GOOGLE_SLIDES = 'com.google.android.apps.docs.app.NewMainProxyActivity'
    ADOBE = '.AdobeReader'
    MORELANGS = 'sightidea.com.setlocale.LocaleActivity'
    GOOGLE_CHROME = 'com.google.android.apps.chrome.Main'
    WPRINT_TEST = "com.hp.droid.automationapp.TestActivity"
    DROPBOX_HOME = "com.dropbox.android.activity.DbxMainActivity"
    HPBRIDGE = ".ui.LauncherUI"
    WPRINT_DEBUG = "com.hp.wprint.debug.enabler.ActivityDebugEnabler"
    GOOGLE_PLAY = 'com.google.android.finsky.activities.MainActivity'
    MICROSOFT_EXCEL = 'com.microsoft.office.apphost.LaunchActivity'
    JWEB = 'com.hp.jarvisreference.MainActivity'
    JWEB_DATA_COLLECTION = 'com.hp.jarvis.datacollectionexample.MainActivity'

class WAIT_ACTIVITY():
    DROPBOX = 'com.dropbox.android.activity.DbxMainActivity, ' \
              'com.dropbox.android.activity.LoginOrNewAcctActivity, ' \
              'com.dropbox.android.onboarding.CuOnboardingActivity, ' \
              'com.dropbox.android.paywall.PaywallActivity,' \
              'com.dropbox.android.activity.payment.PaymentSelectorActivity,' \
              'com.dropbox.product.dbapp.desktoplink.DesktopLinkActivity'
    # Apparently google docs, sheets, slides use the same relative path
    APP_DOC = 'com.google.android.apps.docs*'

class OPTIONAL_INTENT_ARGUMENTS():
    HPPS = "--es activity-flow /automation"

class RESULTS():
    RESULTS_FOLDER = ma_misc.get_abs_path("/results", False)

class TEST_DATA():
    SMART_APP_LOG_PATH = "/sdcard/Android/data/com.hp.printercontrol.debug/files/logs/"
    HPPS_APP_LOG_PATH = "/sdcard/Android/data/com.hp.android.printservice/files/logs/"
    MOBILE_DOWNLOAD = "/sdcard/Download"
    MOBILE_PICTURES = "/sdcard/Pictures"
    GMAIL_TOKEN_PATH = "/qama/framework/data/gmail.token"
    GDRIVE_TOKEN_PATH = "/resources/test_data/clouds/gdrive_token.json"
    GMAI_ACCOUNT = "/resources/test_data/email/account.json"
    HPID_ACCOUNT = "/resources/test_data/hpid/account.json"
    CLOUD_ACCOUNT = "/resources/test_data/clouds/account.json"
    SOFTFAX_ACCOUNT = "/resources/test_data/softfax/account.json"
    DOCUMENTS_PDF_FOLDER = "/resources/test_data/documents/pdf"
    IMAGES_JPG_FOLDER = "/resources/test_data/images/jpg"
    ONE_PAGE_PDF = "1page.pdf"
    BOW_JPG = "bow.jpg"
    JPG_WORM = "worm.jpg"
    PDF_1PAGE_1MB = "1page_1mb.pdf"
    PDF_1PAGE_3MB = "1page_3mb.pdf"
    PDF_2PAGES_20MB = "2pages_20mb.pdf"
    PDF_4PAGES_12MB = "4page_12mb.pdf"
    PDF_10PAGES_20MB = "10pages_20mb.pdf"
    PDF_BIG_PDF_30MB = "big_pdf_30mb.pdf"
    PDF_MORE_THAN_50PAGES = "more_than_50pages.pdf"
    PDF_3PAGES_WORD_IMAGE = "3page_word_image.pdf"
    PDF_5PAGES_EMAIL = "5page_email.pdf"
    PDF_6PAGES_FORMATTED_DOC = "6page_formatted_document.pdf"
    HPBRIDGE_TEST_DEVICE = "/resources/test_data/hpbridge/devices.json"
    HPBRIDGE_TEST_ACCOUNT = "/resources/test_data/hpbridge/accounts.json"
    HPBRIDGE_TEST_STACK = "/resources/test_data/hpbridge/stack_info.json"
    HPBRIDGE_TEST_PRINTER = "/resources/test_data/hpbridge/printers.json"
    JWEB_ACCOUNT = "/resources/test_data/jweb/account.json"

class GOOGLE_PHOTOS():
    DEFAULT = "png"
    PNG = "png"
    JPG = "jpg"
    JPEG = "jpeg"

class GOOGLE_DOCS():
    DOCX_1 = "1page.docx"
    FILE_EXTENSION = "docx"


class EXCEL():
    XLS_1 = "1page.xls"
    FILE_EXTENSION = "xls"


class GOOGLE_SHEETS():
    XLS_1 = "1page.xls"
    FILE_EXTENSION = "xls"


class GOOGLE_DRIVE():
    PDF_1 = "1page.pdf"
    FILE_EXTENSION = "pdf"


class GOOGLE_SLIDES():
    PPT_1 = "1page.ppt"
    FILE_EXTENSION = "ppt"


class ADOBE():
    PDF_1 = "1page.pdf"
    FILE_EXTENSION = "pdf"

class CHROME():
    FILE_EXTENSION = "html"


class FACEBOOK_ALBUM():
    MOBILE_UPLOADS = "Mobile Uploads"


class ANDROID_PROCESS:
    HPBRIDGE = "com.tencent.mm:tools"


class CUSTOM_CHROME_DRIVER:
    HPBRIDGE = ma_misc.get_abs_path("/resources/test_data/driver/2_37/chromedriver")
    #JWEB = ma_misc.get_abs_path("/resources/test_data/driver/84/chromedriver")

class DROPBOX():
    DOCUMENT_FOLDER = "testdata_cloud/documents"
    IMAGE_FOLDER = "testdata_cloud/images"
    PDF_1PAGE_1MB = "1page_1mb.pdf"
    PDF_1PAGE_3MB = "1page_3mb.pdf"
    PDF_2PAGES_20MB = "2pages_20mb.pdf"
    PDF_4PAGES_12MB = "4page_12mb.pdf"
    PDF_10PAGES_20MB = "10pages_20mb.pdf"
    PDF_BIG_PDF_30MB = "big_pdf_30mb.pdf"
    JPG_BOW = "bow.jpg"
    JPG_WORM = "worm.jpg"
    PNG_FISH = "fish.png"