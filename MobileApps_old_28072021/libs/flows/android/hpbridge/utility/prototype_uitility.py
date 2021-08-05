# coding: utf-8
import enum
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow


class PrinterInfo(object):

    def __init__(self, default_device=None, device_group="客厅", role=None,
                 device_id=None, model_name=None, device_name=None, doc_setting=None, img_setting=None, printer_json=None):
        """
        init the printer's info
        :param default_device: True if it is bound as default printer
        :param device_group: the group info
        :param role: the user's role for this printer, "admin" or "user"
        :param device_id: the printer's device id in bridge DB
        :param model_name: the printer's model name
        :param device_name: the printer's customised name when it was bound
        :param doc_setting: the printer's customised document print settings
        :param img_setting: the printer's customised picture print settings
        """
        if not printer_json:
            self.default_device = default_device
            self.device_group = device_group
            self.role = role
            self.device_id = device_id
            self.model_name = model_name
            self.device_name = device_name
            self.doc_setting = doc_setting
            self.img_setting = img_setting
        else:
            self.default_device = printer_json["defaultDevice"]
            self.device_group = printer_json["deviceGroup"]
            self.device_id = printer_json["deviceId"]
            self.model_name = printer_json["deviceModelName"]
            self.device_name = printer_json["deviceName"]
            self.role = printer_json["role"]

            if printer_json["printSetting"] is not None and printer_json["printSetting"] != "{}":
                self.doc_setting = PrintSetting(setting_json=printer_json["printSetting"]["doc"])
                self.img_setting = PrintSetting(setting_json=printer_json["printSetting"]["photo"])


class PrintSetting(object):

    def __init__(self, max_copies="50", duplex=None, media_size=None, media_type=None, color=None, quality=None,
                 setting_json=None):
        """
         the print settings
        :param max_copies: the mac copies when print
        :param plex: the plex settings
        :param media_size: the print paper size
        :param media_type: the print paper type
        :param color: color print or not
        :param quality: the print quality
        """
        if not setting_json:
            self.max_copies = max_copies
            self.duplex = duplex
            self.media_size = media_size
            self.media_type = media_type
            self.color = color
            self.quality = quality
        else:
            for item in setting_json:
                if item["type"] == "MaxCopies":
                    self.max_copies = item["defaultValue"]
                elif item["type"] == "Plex":
                    self.duplex = item["defaultValue"] == "Duplex"
                elif item["type"] == "MediaSize":
                    if item["defaultValue"] == "IsoA4_210x297mm":
                        self.media_size = HPBridgeFlow.print_options_dict["A4"]
                    elif item["defaultValue"] == "NaIndex_4x6_4x6in":
                        self.media_size = HPBridgeFlow.print_options_dict["4x6"]
                    else:
                        self.media_size = HPBridgeFlow.print_options_dict["5x7"]
                elif item["type"] == "MediaType":
                    if item["defaultValue"] == "HPGlossy220":
                        self.media_type = HPBridgeFlow.print_options_dict["HPGlossy220"]
                    else:
                        self.media_type = HPBridgeFlow.print_options_dict["Plain"]
                elif item["type"] == "Color":
                    self.color = item["defaultValue"] == "Color"
                elif item["type"] == "Quality":
                    if item["defaultValue"] == "FastDraft":
                        self.quality = HPBridgeFlow.print_options_dict["draft"]["tag"]
                    elif item["defaultValue"] == "Normal":
                        self.quality = HPBridgeFlow.print_options_dict["normal"]["tag"]
                    else:
                        self.quality = HPBridgeFlow.print_options_dict["best"]["tag"]


class SupplyInfo(object):
    def __init__(self, score=0, status=None, m_cartridge=None, c_cartridge=None, y_cartridge=None,
                 k_cartridge=None, cmy_cartridge=None, supply_json=None):
        """
        all cartridges information for the printer
        :param score: the supply state score
        :param status: the supply status
        :param m_cartridge: the M cartridge information, is object of class Cartridge
        :param c_cartridge: the C cartridge information, is object of class Cartridge
        :param y_cartridge: the Y cartridge information, is object of class Cartridge
        :param k_cartridge: the K cartridge information, is object of class Cartridge
        :param cmy_cartridge: the CMY cartridge information, is object of class Cartridge
        """
        if not supply_json:
            self.score = score
            self.status = status
            self.m_cartridge = m_cartridge
            self.c_cartridge = c_cartridge
            self.y_cartridge = y_cartridge
            self.k_cartridge = k_cartridge
            self.cmy_cartridge = cmy_cartridge
        else:
            self.score = supply_json["statistics"]["score"]
            self.status = supply_json["statistics"]["status"]
            for item in supply_json["supplyInfos"]:
                if item["type"] == "all":
                    continue
                cartridge = Cartridge(cartridge_json=item)
                if cartridge.color == "M":
                    self.m_cartridge = cartridge
                elif cartridge.color == "C":
                    self.c_cartridge = cartridge
                elif cartridge.color == "Y":
                    self.y_cartridge = cartridge
                elif cartridge.color == "K":
                    self.k_cartridge = cartridge
                elif cartridge.color == "CMY":
                    self.cmy_cartridge = cartridge
                else:
                    raise KeyError("Unsupported cartridge")


class Cartridge(object):
    def __init__(self, color=None, part_info=None, remaining_percent=None, state=None, type=None, cartridge_json=None):
        """
        the cartridge information
        :param color:
        :param part_info:
        :param remaining_percent:
        :param state:
        :param type:
        """
        if not cartridge_json:
            self.color = color
            self.part_info = part_info
            self.remaining_percent = remaining_percent
            self.state = state
            self.type = type
        else:
            self.color = cartridge_json["color"]
            self.part_info = cartridge_json["partInfo"]
            self.remaining_percent = cartridge_json["remainingPercent"]
            self.state = cartridge_json["state"]
            self.type = cartridge_json["type"]


class PrinterNameOption(enum.Enum):
    HOME = '家庭打印机'
    OFFICE = '办公室打印机'
    FRIEND = '好友的打印机'
    PUBLIC = '公共打印机'


class PrinterStatus(enum.Enum):
    READY = '可用'
    SEARCHING = '查询中'
    NOT_AVAILABLE = '不可用'
    UNKNOWN = '未知'
    OFFLINE = '离线'
    RESET = '已重置'


class SupplyStatus(enum.Enum):
    NotSupport = "printer not support"
    Error = "get supply error"


class PrintResult(enum.Enum):
    PRINT_COMPLETED = '打印完毕通知'
    PRINT_FAILED = '打印状态提醒'


class PrintJobStatus(enum.Enum):
    PRINT_INPROGRESS = "iconfont icon-process process"
    PRINT_PASSED = "iconfont icon-success success"
    PRINT_FAILED = "iconfont icon-error error"


class PageTitle(enum.Enum):
    SUPPLY_PURCHASE = "购买耗材"
    HP_SUPPLY_POINTS = "惠普耗材积分"
    NEW_FUNCTION_INTRODUCTION = "新功能介绍"
    WECHAT_PRINT_NOTICE = "微信打印须知"
    CONTACT_SUPPORT = "联系客服"
    SUGGESTION_BOX = "意见箱"
    HP_SUPPLY_CLUB_APP_NAME = "惠普原装耗材积分俱乐部"
    FIRST_TIME_BINDING_PRINTER = "首次绑定打印机"
    PAGE_FUNCTION_INTRODUCTION = "页面功能介绍"


class GroupName(enum.Enum):
    LIVING_ROOM = "客厅"
    BED_ROOM = "卧室"
    STUDY = "书房"


class MessageCenter(enum.Enum):
    PRINT_SUCCESS_NOTIFICATION = "打印成功通知"
    PRINT_FAILED_NOTIFICATION = "打印失败通知"
    PRINTER_BINDING_NOTIFICATION = "打印机绑定通知"
    PRINTER_UNBIND_NOTIFICATION = "打印机解绑通知"
    PRINTER_BINDING_REMIND = "打印机绑定提醒"


class PrintQuality(enum.Enum):
    DRAFT = "草稿"
    NORMAL = "一般"
    BEST = "最佳"


class PrintPreviewFileName(enum.Enum):
    WEB_ARTICLE = "网络文章.pdf"