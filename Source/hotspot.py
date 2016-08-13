import requests, urllib, time, getpass, schedule, signal
from datetime import datetime

user_data = dict()

# Taken from http://stackoverflow.com/a/8019156
def check_connectivity(reference):
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False

def login():
    URL = 'https://authenticate.upm.my:801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null&wlanacname=null&port=&iTermType=1&mac=000000000000&redirect=null&session=null'
    payload = {
        'DDDDD': user_data['username'],
        'upass': user_data['password'],
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
    #session = requests.session()
    requests.post(URL, data=payload)
    time.sleep(2)

def network_check():
    while (not check_upm_wifi()):
        print("Retrying in 5 seconds...")
        time.sleep(5)
    if check_connectivity("https://google.com/"):
        print( "[" + str(datetime.now()) + "] Network status: OK")
    else:
        print( "[" + str(datetime.now()) + "] Network status: ERROR")
        time.sleep(2)
        print( "[" + str(datetime.now()) + "] Network status: RECONNECTING...")
        login()
        network_check()

def check_upm_wifi():
    if not check_connectivity("https://authenticate.upm.my/"):
        print("You're not connected to Hotspot@PUTRA")
        return False
    else:
        return True

def main():
        #print(sys.argv)
    try:
        user_data['username'] = input("UPM ID: ")
        user_data['password'] = getpass.getpass(prompt='Password: ')
        print("\n === Press CTRL+C to exit (2 times to force exit) ===\n")
    except:
        print("Invalid input")
        exit(100)
    try:
        while (not check_upm_wifi()):
            print("Retrying in 5 seconds...")
            time.sleep(5)
        login()
        if check_connectivity("https://ijat.my/"):
            print( "[" + str(datetime.now()) + "] Network status: OK")
        else:
            print( "[" + str(datetime.now()) + "] Network status: ERROR -- Please reenter your login credential.")
            time.sleep(2)
            main()
    except:
        main()

    schedule.every(5).seconds.do(network_check)

    while True:
        schedule.run_pending()
        time.sleep(30)
        

if __name__ == '__main__':
    def signal_handler(signal, frame):
        print('* Exiting...')
        exit()
    signal.signal(signal.SIGINT, signal_handler)
    print("\nHotspot@Putra Auto-Login v0.1\n\tby Ijat.my\n")
    try:
        main()
    except:
        exit(1)
