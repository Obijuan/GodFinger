#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

#-- Servo angular speed, in deg/seg (Futaba 3003)
ServoW = 260.0

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
       
    #-- TODO: check that pos in in the range [-90,90]   
       
    #-- Build the frame   
    frame = ":" + str(self.dir) + "P" + str(pos) + " "
    
    #-- Debug
    print frame
    
    #-- Send the frame
    self.sp.write(frame)
    
    #-- Wait some time, for the servo to reach the target position
    #-- Stimated time:
    stime = abs(pos - self._pos) / ServoW
    #print "Time: {0}".format(stime)  #-- Debug
    time.sleep(stime)
    
    #-- Store the current servo pos
    self._pos = pos
    
    