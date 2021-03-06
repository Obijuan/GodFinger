#!/usr/bin/python
# -*- coding: utf-8 -*-

import getopt
import sys
import serial
from Servo import *
from Finger import *

# parse command line options
try:
  opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
except getopt.error, msg:
  print msg
  print "for help use --help"
  sys.exit(2)
  
# process options
for o, a in opts:
  if o in ("-h", "--help"):
    print __doc__
    sys.exit(0)

#-- Default serial port (if none is given in the arguments)
serial_name = "/dev/ttyUSB0"

#-- If there are arguments...
if (len(args) > 0) :
    
  #-- The first arg. is the serial port
  serial_name = args[0]

#print "Puerto serie: {0}".format(serial_name)

#-- Open the serial port
#--------------------------------------------------------
#-- Abrir el puerto serie. Si hay algun error se termina
#--------------------------------------------------------
try:
  s = serial.Serial(serial_name, 115200)
  
  #-- Timeout: 100 ms
  s.timeout=0.1;

except serial.SerialException:
  #-- Error al abrir el puerto serie
  sys.stderr.write("Error opening the port {0}".format(serial_name))
  sys.exit(1)

#-- Mostrar el nombre del dispositivo
print "Puerto serie abierto: {0}\n".format(s.name)


#-- Create the servos to use
#s1 = Servo(s, 2)
#s2 = Servo(s, 4)

f1 = Finger(s, 2, up = 68, down = 76)
f2 = Finger(s, 4, up = 65, down = 74)

#-- Put the fingers in the up position
f1.up()
f2.up()



