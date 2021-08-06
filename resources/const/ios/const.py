#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MobileApps.libs.ma_misc import ma_misc


# NOT SUGGESTIBLE BUT FOLLOWING,, FOR EASY RECOGNISE BY LOOKS WISE
# Creating this newly to keep matches with visible name on app and trying to keep in clean format
# Trying to keep class names as all CAPITAL and under class the variables also all CAPITAL.
# following this to easy understand when we see all capitals in method parameter passing::means that is defined in const


class NONE_THIRD_PARTY_APP():
    APP_LIST = ["SMART", "JWEB", "JAUTH", "JWEB_DATA_COLLECTION"]


class HOME_TILES():
    TILE_INSTANT_INK = "_shared_instant_ink_tile"
    TILE_PLAY_LEARN = "_shared_play_learn_tile"
    TILE_SMART_TASK = "_shared_smart_task_tile"
    TILE_CAMERA_SCAN = "_shared_camera_scan_tile"
    TILE_HELP_AND_SUPPORT = "_shared_help_tile"
    TILE_PRINT_PHOTOS = "_shared_print_photos_tile"
    TILE_PRINT_DOCUMENTS = "_shared_print_documents_tile"
    TILE_SCAN = "_shared_scan_tile"
    TILE_COPY = "_shared_copy_tile"
    TILE_CREATE_PHOTOS = "_shared_create_photos_tile"
    TILE_MOBILE_FAX = "_shared_mobile_fax_tile"


class SCAN_SETTINGS():
    INPUT_SOURCE = "_const_input_src_btn"
    QUALITY = "_const_quality_btn"
    COLOR = "_const_color_btn"


class SCAN_INPUT_SOURCE():
    AUTOMATIC = "_const_input_src_automatic_btn"
    SCANNER_GLASS = "_const_input_src_scanner_glass_btn"
    DOCUMENT_FEEDER = "_const_input_src_doc_feeder_btn"


class SCAN_QUALITY():
    NORMAL = "_const_quality_normal_btn"
    DRAFT = "_const_quality_draft_btn"
    BEST = "_const_quality_best_btn"


class SCAN_COLOR():
    BLACK = "_const_black_btn"
    COLOR = "_const_color_option_btn"
    GRAYSCALE = "_const_grayscale_btn"


class SCAN_PAPAER_SIZES():
    A4 = "_const_paper_size_a4_option"
    LETTER = "_const_paper_size_letter_option"
    SIZE_3X5 = "_const_paper_size_3_5x5_option"
    SIZE_5X7 = "_const_paper_size_5x7_option"
    SIZE_4X6 = "_const_paper_size_4x6_option"
    CUSTOM_SIZE = "_const_paper_size_custom_size_option"
    A3 = "_const_paper_size_a3_option"
    US_LEGAL = "_const_paper_us_legal_option"


class PREVIEW_FILE_TYPE():
    PDF = "_const_file_type_pdf"
    JPG = "_const_file_type_jpg"


class SCAN_EDIT_CROP():
    FREEFORM = "_const_crop_free_form"
    A4 = "_const_crop_a4_btn"
    SQUARE = "_const_crop_square_btn"
    LETTER = "_const_crop_letter_btn"
    SIZE_5x7 = "_const_crop_5x7_btn"
    SIZE_4x6 = "_const_crop_4x6_btn"
    SIZE_3X5X5 = "_const_crop_3.5x5_btn"


class SCAN_EDIT_ROTATE():
    LEFT = "_const_rotate_left_btn"
    RIGHT = "_const_rotate_right_btn"
    FLIPH = "_const_rotate_flip_h_btn"
    FLIPV = "_const_rotate_flip_v_btn"


class PREVIEW_SAVE_FILE_SIZES():
    ACTUAL_SIZE = "_const_save_actual_size"
    MEDIUM_SIZE = "_const_save_medium_size"
    SMALL_SIZE = "_const_save_small_size"


class PRINT_EDIT_PRINT_QUALITY():
    DRAFT = "_const_color_quality_draft"
    NORMAL = "_const_color_quality_normal"
    BEST = "_const_color_quality_best"


class PRINT_EDIT_COLOR_OPTION():
    COLOR = "_const_color"
    BLACK_ONLY = "_const_black_only"
    GRAY_SCALE = "_const_gray_scale"


class PRINT_EDIT_TWO_SIDED():
    OFF = "_const_two_side_off"
    SHORT_EDGE = "_const_short_edge"
    LONG_EDGE = "_const_long_edge"


class PRINT_EDIT_RESIZE():
    ORIGINIAL_SIZE = "_const_original_size"
    FIT_TO_PAGE = "_const_fit_to_size"
    FILL_PAGE = "_const_fill_size"


class OBJECT_SIZE():
    SIZE_LETTER = "_shared_paper_size_letter"
    SIZE_US_LEGAL = "_shared_us_legal"
    SIZE_4x6 = "_shared_paper_size_4x6"
    SIZE_5x7 = "_shared_paper_size_5x7"
    SIZE_DRIVER_LICENSE = "_shared_driver_license"
    SIZE_BUSINESS_CARD = "_shared_business_card"


class RESIZE():
    RESIZE_ORIGINAL_SIZE = "_shared_original_size"
    RESIZE_FIT_TO_PAGE = "_shared_fit_to_page"
    RESIZE_FILL_PAGE = "_shared_fill_page"


class PRINT_EDIT_RESIZE_AND_MOVE():
    MANUAL = "_const_resize_manual"
    ORIGINAL_SIZE = "_const_resize_original_size"
    FIT_TO_PAGE = "_const_resize_fit_to_page"
    FILL_PAGE = "_const_resize_fill_page"


class BUNDLE_ID():
    SETTINGS = "com.apple.Preferences"
    HOME = "com.apple.Home"
    SMART = "com.hp.printer.control.dev"
    JAUTH = "com.hp.jarvis.auth.example"
    JWEB = "com.hp.jarvis.JWebReference"
    JWEB_DATA_COLLECTION = "com.hp.jarvis.datacollection.example"
    FILES = "com.apple.DocumentsApp"

class FLASH_MODE():
    FLASH_OFF = "flash_off"
    FLASH_ON = "flash_on"
    FLASH_TORCH = "flash_torch"
    FLASH_AUTO = "flash_auto"


class TEST_DATA():
    GMAIL_TOKEN_PATH = "/qama/framework/data/gmail.token"
    GMAIL_ACCOUNT = "/resources/test_data/email/account.json"
    HPID_ACCOUNT = "/resources/test_data/hpid/account.json"
    SOFTFAX_ACCOUNT = "/resources/test_data/softfax/account.json"
    TEST_ACCOUNT = "/resources/test_data/hpid/test_accounts.json"


class WEBVIEW_URL():
    VALUE_PROP = "ucde/account-prop"
    HPID = "id.hp.com/login3"
    SMART_WELCOME = "in-app/ios"
    SOFTFAX_OFFER = "in-app/mobile-fax"
    SOFTFAX = "sws"
    HP_CONNECT = "/ucde"
    SERVICE_ACCOUNT = "api-sgw.external.hp.com"