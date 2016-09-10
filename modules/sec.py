#!/usr/bin/python

import sys


class MyException(Exception):
    pass


class SecFile:
    def __init__(self):
        try:
            __file = open(".dat", "r")
            __str = __file.read()
        except Exception:
            pass
            # raise MyException("My hovercraft is full of eels")
