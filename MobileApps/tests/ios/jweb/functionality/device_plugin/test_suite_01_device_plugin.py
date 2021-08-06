import pytest

pytest.app_info = "JWEB"

class Test_Suite_01_Device_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.device_plugin = cls.fc.fd["device_plugin"]

        # Language codes as of ISO 639-1
        cls.languages = ['aa', 'ab', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'ba', 'bm', 'eu', 'be', 'bn',
                     'bh', 'bi', 'bo', 'bs', 'br', 'bg', 'my', 'ca', 'cs', 'ch', 'ce', 'zh', 'cu', 'cv', 'kw', 'co', 'cr', 'cy', 'cs',
                     'da', 'de', 'dv', 'nl', 'dz', 'el', 'en', 'eo', 'et', 'eu', 'ee', 'fo', 'fa', 'fj', 'fi', 'fr', 'fy', 'ff', 'ga',
                     'de', 'gd', 'ga', 'gl', 'gv', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hr', 'hu', 'hy', 'ig', 'is',
                     'io', 'ii', 'iu', 'ie', 'ia', 'id', 'ik', 'is', 'it', 'jv', 'ja', 'kl', 'kn', 'ks', 'ka', 'kr', 'kk', 'km', 'ki',
                     'rw', 'ky', 'kv', 'kg', 'ko', 'kj', 'ku', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'lb', 'lu', 'lg', 'mk', 'mh', 'ml',
                     'mi', 'mr', 'ms', 'mi', 'mk', 'mg', 'mt', 'mn', 'mi', 'ms', 'my', 'na', 'nv', 'nr', 'nd', 'ng', 'ne', 'nl', 'nn',
                     'no', 'oc', 'oj', 'or', 'om', 'os', 'pa', 'fa', 'pi', 'pl', 'pt', 'ps', 'qu', 'rm', 'ro', 'ro', 'rn', 'ru', 'sg', 
                     'sa', 'si', 'sk', 'sk', 'sl', 'se', 'sm', 'sn', 'sd', 'so', 'st', 'es', 'sq', 'sc', 'sr', 'ss', 'su', 'sw', 'sv', 
                     'ty', 'ta', 'tt', 'te', 'tg', 'tl', 'th', 'bo', 'ti', 'to', 'tn', 'ts', 'tk', 'tr', 'tw', 'ug', 'uk', 'ur', 'uz', 
                     've', 'vi', 'vo', 'cy', 'wa', 'wo', 'xh', 'yi', 'yo', 'za', 'zh', 'zu']

    def test_01_verify_device_info(self):
        """
        verify pressing the test button in Device.getInfo() returns the information of a device
        
        TestRails -> C28698083
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_device_plugin()
        self.device_plugin.press_device_info_test_btn()
        device_info = self.device_plugin.return_device_info()
        assert device_info["platform"] == "ios" 
        assert device_info["model"] != ""
        assert device_info["osVersion"] != ""

    def test_02_verify_device_language_code(self):
        """
        verify pressing the test button in Device.getLanguageCode() returns the device's current language locale code
        
        TestRails -> C28698084
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_device_plugin()
        self.device_plugin.press_language_test_btn()
        language_code = self.device_plugin.return_language_test_result()['value']
        assert language_code[:2].lower() in self.languages