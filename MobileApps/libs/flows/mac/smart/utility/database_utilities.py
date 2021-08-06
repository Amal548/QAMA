# encoding: utf-8
'''
Description: It defines miscellaneous which are used to operation database.

@author: Sophia
@create_date: Aug 15, 2019
'''

from abc import ABCMeta, abstractmethod
import MySQLdb
import logging

from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import ItemNotFoundException


class DataBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, db_info_dict):
        self.db_url = db_info_dict["url"] + ":" + db_info_dict["port"]
        self.db_user = db_info_dict["user"]
        self.db_pw = db_info_dict["password"]
        self.db_schema = db_info_dict["database"]
        if "driver" in db_info_dict:
            self.db_connection = db_info_dict["driver"]

    def connect(self):
        if self.db_connection is None:
            if self.db_url:
                try:
                    self.db_connection = MySQLdb.connect(self.db_url, self.db_user, self.db_pw, self.db_schema)
                except MySQLdb.Error as sqle:
                    logging.error("Failed to connect DB.")
                    raise ItemNotFoundException("SQL Exception - " + sqle.getMessage())
            else:
                raise ItemNotFoundException("dbURL parameter is missing.")
        if self.db_connection is None:
            raise ItemNotFoundException("Failed to connect to Database.")

    def disconnect(self):
        if self.db_url is not None and self.db_connection is not None:
            try:
                self.db_connection.close()
                self.db_connection = None
            except MySQLdb.Error as sqle:
                    logging.error("Failed to disconnect DB.")
                    raise ItemNotFoundException("SQL Exception - " + sqle.getMessage())

    def reconnect(self):
        self.disconnect()
        self.connect()


class DataBaseFunctions(DataBase):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, db_info_dict):
        super(DataBaseFunctions, self).__init__(db_info_dict)

    def execute_update(self, sql_update):
        to_return = -1
        self.connect()

        try:
            cursor = self.db_connection.cursor()
            to_return = cursor.execute(sql_update)
            self.db_connection.commit()
            cursor.close()
        except MySQLdb.Error as sqle:
            logging.error("Failed to run update " + sql_update)
            self.db_connection.rollback()
            raise ItemNotFoundException("SQL Exception - " + sqle.getMessage())
        finally:
            logging.debug("Total Number of " + to_return + " records were updated in DB")
            self.disconnect()
        return to_return

    def execute_query_data(self, sql_query):
        self.connect()

        try:
            cursor = self.db_connection.cursor()
            cursor.execute(sql_query)
            to_return_data = cursor.fetchone()
            cursor.close()
        except MySQLdb.Error as sqle:
            logging.error("Failed to run query " + sql_query)
            raise ItemNotFoundException("SQL Exception - " + sqle.getMessage())
        finally:
            self.disconnect()
        return to_return_data

    def execute_query_all_datas(self, sql_query):
        self.connect()

        try:
            cursor = self.db_connection.cursor()
            cursor.execute(sql_query)
            to_return_datas = cursor.fetchall()
            cursor.close()
        except MySQLdb.Error as sqle:
            logging.error("Failed to run query " + sql_query)
            raise ItemNotFoundException("SQL Exception - " + sqle.getMessage())
        finally:
            self.disconnect()
        return to_return_datas
