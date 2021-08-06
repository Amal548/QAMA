class VERSION():
    V5_10 = "5.10"


class Gmail(object):
    @staticmethod
    def create_flow(app, cfg, ui):
        """
        Create a flow of Gmail based on version
        :param app: appium server
        :type app: MobiEzApp
        :param cfg: configuration
        :type cfg: MobiConfig
        :param ui: ui map object
        :type ui: MobiUiMap
        :return: object Activate
        """
        from MobileApps.flows.android.gmail.v5_10.gmail_v5_10 import Gmail_v5_10
        GMAIL = {
            VERSION.V5_10: Gmail_v5_10
        }

        return GMAIL[ui.get_version()](app, cfg, ui)
