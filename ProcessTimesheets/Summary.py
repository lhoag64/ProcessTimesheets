#import os
#import datetime
import logging
from   Calendar  import Calendar
from   TimeSheet import Timesheet
#from openpyxl import load_workbook


#-----------------------------------------------------------------------
# Class TSSummary
#-----------------------------------------------------------------------
class TSSummary:
  def __init__(self):
    self.sslist = []
    self.tsdict = {}
    self.week = None
    self.year = None

  #---------------------------------------------------------------------
  def Process(self,tsdata,team,year,week):
    self.year = year
    self.week = week

    cal = Calendar(year)
    self.Sort(tsdata,cal,week)

    for i,week in enumerate(self.sslist):
      wsDate = cal.week[i+1]
      logging.debug('***' + str(wsDate) + '***')
      self.tsdict[wsDate] = []
      for j,ssdata in enumerate(week):
        ts = Timesheet(ssdata, wsDate)
        ts.ReadFile()
        ts.Clean()
        self.tsdict[wsDate].append(ts)
      logging.debug('***' + str(wsDate) + '***')

  #-----------------------------------------------------------------------
  def Sort(self,tsdata,cal,week):
    self.sslist = []
    for i in range(1,week+1):
      list = []
      dict = {}
      wsDate = cal.week[i]
      logging.debug(str(i) + ' ' + str(wsDate))
      dict = tsdata.weeks[wsDate]
      for key,value in dict.items():
        list.append(value)
      self.sslist.append(sorted(list))
 
    for i,week in enumerate(self.sslist):
      logging.debug(cal.week[i+1])
      for j,item in enumerate(week):
        logging.debug(item.fae.team + ' ' + item.fae.loc + ' ' + item.fae.fullname)
        
    logging.debug('sorted list')






