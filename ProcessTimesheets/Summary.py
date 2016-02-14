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

    self.Sort(tsdata,week)

    for i,week in enumerate(self.sslist):
      wsDate = Calendar.week[i+1]
      self.tsdict[wsDate] = []
      for j,ssdata in enumerate(week):
        #logging.debug(ssdata.
        ts = Timesheet(ssdata, wsDate)
        ts.ReadFile()
        self.tsdict[wsDate].append(ts)

    for i in range(1,self.week+1): 
      wsDate = Calendar.week[i]
      tslist = self.tsdict[wsDate]
      for j in tslist:
        faeName = j.ssdata.fae.fullname.ljust(21)
        faeType = j.ssdata.fae.laborType
        faeTeam = j.ssdata.fae.team.ljust(3)
        faeLoc  = j.ssdata.fae.loc
        ws      = str(j.ssdata.wsDate)
        we      = str(j.ssdata.weDate)
        for k in j.entries:
          wDate  = str(k.date)
          wCode  = str(k.code).ljust(5)
          wLoc   = str(k.location).ljust(3)
          wAct   = str(k.activity).ljust(2)
          wProd  = str(k.product).ljust(2)
          wHours = str(k.hours).ljust(5)
          wLtd   = str(k.workType).ljust(10)
          logging.debug \
            (faeName + '|' + faeType + '|' + faeTeam + '|' + faeLoc + '|' + \
             ws      + '|' + we      + '|' + wDate   + '|' + \
             wCode   + '|' + wLoc    + '|' + wAct    + '|' + wProd + '|' + \
             wHours  + '|' + wLtd)
    logging.debug('Done') 

  #-----------------------------------------------------------------------
  def Sort(self,tsdata,week):
    self.sslist = []
    for i in range(1,week+1):
      list = []
      dict = {}
      wsDate = Calendar.week[i]
      dict = tsdata.weeks[wsDate]
      for key,value in dict.items():
        list.append(value)
      self.sslist.append(sorted(list))
 
    #for i,week in enumerate(self.sslist):
    #  logging.debug(Calendar.week[i+1])
    #  for j,item in enumerate(week):
    #    logging.debug(item.fae.team + ' ' + item.fae.loc + ' ' + item.fae.fullname)
        
    #logging.debug('sorted list')






