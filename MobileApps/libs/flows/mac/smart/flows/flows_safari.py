# encoding: utf-8
'''
Description: It defines common flows in the hp smart application.

@author: Sophia
@create_date: May 27, 2020
'''

import logging

import MobileApps.resources.const.mac.const as smart_const


class SafariFlows(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver

    def get_safari_app(self):
        '''
        This is a method to get Safari app.
        :parameter:
        :return:
        '''
        logging.debug("Getting Safari app...")

        self.driver.open_app(smart_const.APP_NAME.SAFARI)
