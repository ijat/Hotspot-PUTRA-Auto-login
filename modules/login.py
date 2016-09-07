#!/usr/bin/python3

import uuid, time, socket, os, platform
from aes import *
import requests


class HotspotUPMError(Exception):
    def __init__(self, message):
        self.error = message


class HotspotUPM:
    def __init__(self, u, p):
        self.__password_raw = p

        self.__uid = uuid.uuid5(uuid.NAMESPACE_DNS, u)
        self.__uid = str(self.__uid).replace("-", "")

        __o_aes = AESCipher(self.__uid)
        self.__password = __o_aes.encrypt(p)
        self.__username = u

        self.__host = "authenticate.upm.my"

    def connect(self):
        try:
            try:
                self.__ip = socket.gethostbyname(self.__host)
            except socket.gaierror:
                if not isUp(self.__ip):
                    return False

            URL = 'https://' + self.__host + ':801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null&wlanacname=null&port=&iTermType=1&mac=000000000000&redirect=null&session=null'
            payload = {
                'DDDDD': self.__username,
                'upass': self.__password_raw,
                'R1': 0,
                'R2': 0,
                'R6': 0,
                'para': 0,
                '0MKKey': 123456,
                'buttonClicked': None,
                'redirect_url': None,
                'err_flag': None,
                'username': None,
                'password': None,
                'user': None
            }

            requests.post(URL, data=payload)
            return True

        except Exception as e:
            return False
            # raise HotspotUPMError(self.__host, e)

    def __get_me(self):
        print("Username\t: {0}\nPassword\t: {1}".format(self.__username, self.__password_raw))
        __uid = uuid.uuid5(uuid.NAMESPACE_DNS, self.__username)
        __uid = str(__uid).replace("-", "")

        o_aes = AESCipher(__uid)
        enc_data = o_aes.encrypt(self.__password_raw)
        dec_data = o_aes.decrypt(enc_data)

        print("Encrypted\t: {0}".format(enc_data))
        print("Decrypted\t: {0}".format(dec_data))


def isUp(hostname):
    giveFeedback = False
    if platform.system() == "Windows":
        response = os.system("ping " + hostname + " -n 1 > nul")
    else:
        response = os.system("ping -c 1 " + hostname + " > /dev/null")
    isUpBool = False
    if response == 0:
        isUpBool = True

    return isUpBool