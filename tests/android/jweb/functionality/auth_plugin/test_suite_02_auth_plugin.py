import pytest

pytest.app_info = "JWEB"

class Test_Suite_02_Auth_Plugin_Allow_User_Interaction_Validation(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]

    def test_01_verify_by_disabling_user_interaction_option(self):
        """
        Assert that every combination of AllowUserInteraction is False returns the error 'userInteractionNotAllowed'

        TestRail -> C28698070
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()

        toggle_combinations = [[False, True, False, False, True], [False, True, False, False, False],
                               [False, True, False, True, True], [False, True, False, True, False],
                               [True, True, False, False, True], [True, True, False, False, False],
                               [True, True, False, True, True], [True, True, False, True, False]]
        
        for combination in toggle_combinations:
            self.auth_plugin.control_auth_token_switches(combination)
            self.auth_plugin.select_auth_get_token_test()
            assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userInteractionNotAllowed'