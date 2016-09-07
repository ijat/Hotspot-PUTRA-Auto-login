#!/usr/bin/python3

class splitState:
    def __init__(self, state=False, args=None):
        if (state) and (args):
            commandLineRun(args)
        else:
            guiRun()


def guiRun():
    print("GUI")


def commandLineRun(args):
    print(args);
