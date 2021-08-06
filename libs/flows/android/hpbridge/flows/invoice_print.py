from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow


class InvoicePrint(HPBridgeFlow):
    flow_name = "invoice_print"

    def select_invoice(self, invoice_name):
        """
        using the invoice name to choose an invoice from the list
        :param invoice_name: the invoice name
        :return:
        """
        self.driver.wait_for_object("invoices", format_specifier=[invoice_name]).click()

    def click_confirm_btn(self):
        """
        Click on the confirm button on select a invoice page
        """
        self.driver.wait_for_object("invoice_confirm").click()

    def check_no_invoice_available_prompt(self):
        """
        Check no invoice available prompt message after select confirm button without select a invoice
        """
        self.driver.wait_for_object("no_invoice_available_prompt", timeout=3)
        self.driver.wait_for_object("no_invoice_available_prompt", invisible=True)

    def check_multiple_invoice_selection_prompt(self):
        """
        Select multiple invoice to print at a time, and check the prompt message
        """
        self.driver.wait_for_object("multiple_invoice_selection_prompt", timeout=3)
        self.driver.wait_for_object("multiple_invoice_selection_prompt", invisible=True)

