#!/usr/bin/python
# -*- coding: utf-8 -*-

class Servo(object):
  """Servo class. For accessing to all the Servos"""
  
  def __init__(self, sp, dir = 0):
    """Arguments: serial port and servo number"""
    self.sp = sp     #-- Serial device
    self.dir = dir   #-- Servo number
    self._pos = 0;   #-- Current pos

  def __str__(self):
    str1 = "Servo: {0}\n".format(self.dir)
    str2 = "Serial port: {0}".format(self.sp.name)
    return str1 + str2
  
  def set_pos(self, pos):
    """Set the angular servo pos. The pos is an integer number
       in the range [-90 ,90] """
       
    #-- Build the frame   
    frame = ":" + str(self.dir) + "P" + str(pos) + " "
    print frame
    
    #-- Send the frame
    self.sp.write(frame)
    
    