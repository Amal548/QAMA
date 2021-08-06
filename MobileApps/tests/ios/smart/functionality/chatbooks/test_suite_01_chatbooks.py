import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "SMART"


class Test_Suite_01_Chatbooks(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.personalize = cls.fc.fd["personalize"]
        cls.photo_books = cls.fc.fd["photo_books"]
    
    @pytest.fixture(scope="function", autouse="true")
    def turn_on_network(self, request):
        self.fc.fd["ios_system"].dismiss_software_update_if_visible()
        self.fc.fd["ios_system"].toggle_airplane_mode(on=False)

        def clean_up():
            self.fc.fd["ios_system"].toggle_airplane_mode(on=False)
        request.addfinalizer(clean_up)

    def test_01_landing_screen(self):
        """
        C27655404
        Launch HP smart and tap on Create Photo Books tile
        tap on No Thanks button and verify user is back on home screen
        """
        self.fc.go_home(reset=True)
        self.home.select_tile_by_name(HOME_TILES.TILE_CREATE_PHOTOS)
        self.photo_books.verify_create_photo_books_screen()
        self.photo_books.select_no_thanks_btn()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()

    def test_02_get_my_photobook_btn(self):
        """
        C27655405
        Launch HP smart and tap on Create Photo Books tile
        tap on 'Get My Photo Book' button and verify user redirected to app store
        """
        self.fc.go_home(reset=True)
        self.home.select_tile_by_name(HOME_TILES.TILE_CREATE_PHOTOS)
        self.photo_books.verify_create_photo_books_screen()
        self.photo_books.select_get_my_photobooks_btn()
        ma_misc.poll(lambda: self.driver.wdvr.query_app_state("com.apple.AppStore") == 4, 20)

