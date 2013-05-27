#!/usr/bin/python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------
#-- Finger class
#-- Juan Gonzalez-Gomez (obijuan).  May-2013
#-----------------------------------------------------------------
#-- A finger2 is defined as a servo with only 2 positions: up and down
#-- It can perform task such as tapping
#-----------------------------------------------------------------
from Servo import *

class Finger(Servo):
  """Finger class. Controlling a servo in 2 position: up and down"""
  
  def __init__(self, sp, dir =0, up = 0, down = 10):
    """up: Angle for the not tapping pos
       down: Angle for tapping
       ttime: Tapping time"""
    super(Finger, self).__init__(sp, dir)
    self.up_ang = up
    self.down_ang = down
     
  def up(self):
    """Going to the upper position (not tapping)"""
    
    self.set_pos(self.up_ang)
    
  def down(self):
    """Going to the down position (tapping)"""
    self.set_pos(self.down_ang)
    
  def tap(self, ttime = 0.1):
    self.down()
    time.sleep(ttime)
    self.up()
    
    