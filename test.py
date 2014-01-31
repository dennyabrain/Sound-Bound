import serial, string
import numpy
import os

ser = serial.Serial('/dev/ttyUSB0', 38400)

li = []

while True:
	by = ser.read()
	if by != '\n':
		li.append(by)
	else:
		li_of_strings = string.join(li).split('\t')
		li_of_strings = [ (li_of_strings[i]).replace(' ', '') for i in range(len(li_of_strings)) ]
#		li_of_strings = [ (li_of_strings[i]).replace("\r", '') for i in range(len(li_of_strings)) ]

		li = []

		if len(li_of_strings)<7:
			continue

		x = li_of_strings[1].strip()
		y = li_of_strings[2].strip()
		z = li_of_strings[3].strip()

#		print x, y, z
		
		x = int(x)
		y = int(y)
		z = int(z)

		if y>-11000 and x>11000:
			if z<-7000:
				print"front-right"
				os.system("echo '"+ "2;" +"' | pdsend 3000")
			elif z>7000:			
				print"front-left"
				os.system("echo '"+ "8;" +"' | pdsend 3000")
			else:
				print"forward"
				os.system("echo '"+ "1;" +"' | pdsend 3000")

		elif z<-9000 and y>-12000 and x>-12000:
			print"right"
			os.system("echo '"+ "3;" +"' | pdsend 3000")

		elif z>7000:
			print"left"
			os.system("echo '"+ "7;" +"' | pdsend 3000")

		elif	y>-9000 and x<-11000:
			if z<-7000:
				print"back-right"
				os.system("echo '"+ "4;" +"' | pdsend 3000")
			elif z>1500:
				print"back-left"
				os.system("echo '"+ "6;" +"' | pdsend 3000")
			else:
				print"backward"
				os.system("echo '"+ "5;" +"' | pdsend 3000")
		else:
			print"no tilt"
			#os.system("echo '"+ "notilt;" +"' | pdsend 3000")
