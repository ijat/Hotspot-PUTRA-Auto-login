#!/usr/bin/python

# import subprocess
# import os
import uuid


def get_id():
    z = uuid.uuid5(uuid.NAMESPACE_DNS, "https://ijat.my/")
    z = str(z).replace("-", "")
    return z
    '''#return "ASD31234B1E3G123G12412039DD10293"
if 'nt' in os.name:
    s = subprocess.Popen('GnuWin32\\sbin\\dmidecode.exe -s system-uuid'.split(), stdout=subprocess.PIPE)
    z = s.stdout.read()
    z = str(z).replace("-", "")
    z = str(z).replace("\r\n", "")
    z = uuid.uuid5(uuid.NAMESPACE_DNS, z)
    z = str(z).replace("-", "")
    return z
else:
    # return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())
    return "ASD31234B1E3G123G12412039DD10293"'''
