#import os
import datetime
import logging

#-----------------------------------------------------------------------
class Calendar:

  week    = {}
  wsDates = None
  weDates = None

  def Init(year):
    Calendar.week = {}
    Calendar.wsDates = set()
    Calendar.weDates = set()

    d = datetime.date(year,1,1)
    while (True):
      if (d.weekday() == 0):
        break;
      else:
        d = d + datetime.timedelta(days=1)
    i = 1
    while(True):
      Calendar.week[i] = d
      Calendar.wsDates.add(d)
      Calendar.weDates.add(d+datetime.timedelta(days=6))
      d = d + datetime.timedelta(days = 7)
      if (d.year > year):
        break;
      i += 1
    #logging.debug('Done')
   
  def Log():
    pass
    #cnt = len(Calendar.week)
    #for i in range(1,cnt+1):
    #  logging.debug(str(i) + ' ' + str(week[i])) 
 
