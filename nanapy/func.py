import os
import random
import string
import binascii

class Func:

    @classmethod
    def generate_device_id(cls):
        device_id = cls.random_hex(4) + \
            '-' + cls.random_hex(2) + \
            '-' + cls.random_hex(2) + \
            '-' + cls.random_hex(2) + \
            '-' + cls.random_hex(6)
        return device_id

    @classmethod
    def generate_appsflyer_id(cls):
        appsflyer_id = cls.random_integer(13) + \
            '-' + cls.random_integer(7)
        return appsflyer_id

    @staticmethod
    def random_hex(count):
        return binascii.b2a_hex(
            os.urandom(count)
        ).decode('utf-8').upper()

    @staticmethod
    def random_integer(count):
        return ''.join(
            [random.choice(string.digits) for _ in range(count)]
        )

    @staticmethod
    def random_string(count):
        return ''.join(
            [random.choice(string.ascii_letters) for _ in range(count)]
        )
