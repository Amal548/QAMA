# encoding: utf-8
'''
Description: It defines exceptions which are used in the MAC code.

@author: Sophia
@create_date: July 25, 2019
'''


class ItemTypeError(Exception):
    pass


class ItemNotFoundException(Exception):
    pass


class UnexpectedItemPresentException(Exception):
    pass


class UnexpectedValueException(Exception):
    pass