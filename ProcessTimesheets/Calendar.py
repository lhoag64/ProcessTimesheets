#import os
import datetime
import logging

#-----------------------------------------------------------------------
class Calendar:
  def __init__(self,year):
    self.week = {}
    d = datetime.date(year,1,1)
    while (True):
      if (d.weekday() == 0):
        break;
      else:
        d = d + datetime.timedelta(days=1)
    i = 1
    while(True):
      self.week[i] = d
      d = d + datetime.timedelta(days = 7)
      if (d.year > year):
        break;
      i += 1
   
  def Log(self):
    cnt = len(self.week)
    for i in range(1,cnt+1):
      logging.debug(str(i) + ' ' + str(self.week[i])) 
 
