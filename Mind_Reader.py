 #Copyright (C) 2021 Cennef0x
from serial import *
import os, time, sys
import pandas as pd
import numpy as np


def main():
	global Arduino_Serial
	Arduino_Serial = Serial('com3',9600)  
	os.system('cls')
	time.sleep(2)


main()
 #Copyright (C) 2021 Cennef0x
while True:
	arduino_data = Arduino_Serial.readline() 
	
	decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8")) 
	li = list(decoded_values.split(",")) 
	li_lenght = len(li) 
	
	if li_lenght != 11: 
		pass
	else:	 
		signal_strength = li[0] 
		attention = li[1]  
		meditation = li[2]
		delta = li[3]
		theta = li[4]
		low_alpha = li[5]
		high_alpha = li[6]
		low_beta = li[7]
		high_beta = li[8]
		low_gamma = li[9]
		high_gamma = li[10]

		if int(signal_strength) < 50:
			print("Attention Level {}".format(attention))
		else:
			print("The signal is too weak to obtain good values")
			print("Signal strength : {}\n".format(signal_strength))



arduino.close()
 #Copyright (C) 2021 Cennef0x
