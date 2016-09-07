import urllib, getpass, os, platform
from datetime import datetime


def check_connectivity(reference):
    try:
        urllib.request.urlopen(reference, timeout=5)
        return True
    except urllib.request.URLError:
        return False


def network_check():
    while (not check_upm_wifi()):
        print("Retrying in 5 seconds...")
        time.sleep(5)
    if check_connectivity("https://google.com/"):
        print("[" + str(datetime.now()) + "] Network status: OK")
    else:
        print("[" + str(datetime.now()) + "] Network status: ERROR")
        time.sleep(2)
        print("[" + str(datetime.now()) + "] Network status: RECONNECTING...")
        login()
        network_check()


def check_upm_wifi():
    if not check_connectivity("https://authenticate.upm.my/"):
        print("You're not connected to Hotspot@PUTRA")
        return False
    else:
        return True


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
