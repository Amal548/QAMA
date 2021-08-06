# coding: utf-8
import random


class RandomUtility(object):
    digits = "1234567890"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    special_chars = "~`!@#$%^&* ()_-+=|\\{}[]:;\"',./"

    @staticmethod
    def generate_digit_strs(length):
        return ''.join(random.choice(RandomUtility.digits) for _ in range(length))

    @staticmethod
    def generate_letter_strs(length):
        return ''.join(random.choice(RandomUtility.letters) for _ in range(length))

    @staticmethod
    def generate_digit_letter_strs(length):
        return ''.join(random.choice(RandomUtility.letters + RandomUtility.digits) for _ in range(length))

    @staticmethod
    def generate_special_chars(length):
        return ''.join(random.choice(RandomUtility.special_chars) for _ in range(length))

    @staticmethod
    def generate_strs(length):
        return ''.join(random.choice(RandomUtility.special_chars + RandomUtility.digits + RandomUtility.letters)
                       for _ in range(length))

    @staticmethod
    def generate_chinese(length):
        chinese_str = ''
        for i in range(length):
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xf9)
            val = f'{head:x}{body:x}'
            chinese_str += bytes.fromhex(val).decode('gb2312')
        return chinese_str
