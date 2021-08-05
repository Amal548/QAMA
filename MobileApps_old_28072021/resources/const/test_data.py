from MobileApps.libs.ma_misc import ma_misc

class ANDROID_DEVICE_FILE_LOCATION():
    MOBILE_DOC_PATH = "/sdcard/hpscan/documents"
    MOBILE_IMG_PATH = "/sdcard/hpscan/images"

class TEST_DATA_FILE():
    ONE_PAGE_PDF = ma_misc.get_abs_path("resources/test_data/documents/pdf/1page.pdf")
    BOW_JPG = ma_misc.get_abs_path("resources/test_data/images/jpg/bow.jpg")


class FILE_NAME():
    TEST_FILE_NAME = "test_file"
    TEST_NEW_FILE_NAME ="new_test_file"