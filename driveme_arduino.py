from directkeys import *

import numpy as np 
from time import sleep
import math
from vjoy import look_left,look_right, ultimate_release,throttle

import serial
import time

#arduino = serial.Serial('/dev/ttyACM1', 9600) #Linux
arduino = serial.Serial('COM3', 9600)  #Windows
time.sleep(2)


def PressKeyPWM(val):
    time_down = (512-val)/512

    if np.abs(val) > 512+5 and time_down<0.0:    
        print("right")
        look_left(np.abs(time_down))

    elif np.abs(val) < 512-5 and time_down>0.0:  
        print("left")  
        look_right(np.abs(time_down))

    else:
        print("None")
        ultimate_release()


if __name__=="__main__":
    while 1:
        val = int(arduino.readline())
        print(val)
        PressKeyPWM(val)
