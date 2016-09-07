#!/usr/bin/python3

import time, login, os
from Network import *

class splitState:
    def __init__(self, state=False, args=None):
        if (state) and (args):
            commandLineRun(args)
        else:
            guiRun()


def guiRun():
    print("GUI")


def commandLineRun(args):
    print("\nHotspot@Putra Auto-Login v2.0\n\t   by Ijat.my\n")

    index = 0
    while True:
        netstate = False
        print("[" + str(datetime.now()) + "] Connecting...")
        if isUp("authenticate.upm.my"):
            if not isUp("ijat.my"):
                user = login.HotspotUPM(args.user, args.passwd)
                user.connect()
            else:
                print("[" + str(datetime.now()) + "] Already connected to Hotspot@UPM")
                netstate = True

            while isUp("ping.ijat.my") and isUp("authenticate.upm.my"):
                print("[" + str(datetime.now()) + "] Network OK!")
                time.sleep(30)

        else:
            print("[" + str(datetime.now()) + "] Not connected to Hotspot@UPM (?)")
            index += 1

        if (index > 2) and (args.reset):
            os.system("ifdown ".args.reset)
            os.system("ifup ".args.reset)

        time.sleep(10)


        # print(args);
