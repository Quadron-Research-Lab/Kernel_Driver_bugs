import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "VmSwitch"



ioctl = 0x222008


kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\VmSwitch", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry! Need admin privileges!")

else:
    print ("OPENED!")
                    
    buf = '\x00' * 10000
    bufLength = len(buf)
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

