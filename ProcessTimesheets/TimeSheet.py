#import os
import datetime
import logging
from   openpyxl import load_workbook

 
#-----------------------------------------------------------------------
class TSDate:
  def __init__(self, date):
    self.asStr = str(date)

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class TSCode:
  def __init__(self, partA):
    self.asStr = partA

  def __str__(self): return self.asStr

  def Parse(self): pass
  def Clean (self): pass
  def Log(self): pass

#-----------------------------------------------------------------------
class TSLocation:
  def __init__(self,partB):
    self.asStr = partB

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class TSActivity:
  def __init__(self,partC):
    self.asStr = partC

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class TSProduct:
  def __init__(self,partD):
    self.asStr = partD

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class TSHours:
  def __init__(self,hours):
    self.asStr = str(hours)
    self.asNum = hours

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class TSWorkType:
  def __init__(self,workType):
    self.asStr = workType

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class TSNote:
  def __init__(self,note):
    self.asStr = note

  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
# Class Timesheet Entry
#-----------------------------------------------------------------------
class TSEntry:
  def __init__(self,date,partA,partB,partC,partD,hours,workType,note):
    self.date     = TSDate(date)
    self.code     = TSCode(partA)
    self.location = TSLocation(partB)
    self.activity = TSActivity(partC)
    self.product  = TSProduct(partD)
    self.hours    = TSHours(hours)
    self.workType = TSWorkType(workType)
    self.note     = TSNote(note)

  def Log(self):
    date  = str(self.date)
    partA = str(self.code).ljust(50)     # Customer/Code
    partB = str(self.location).ljust(60) # Location
    partC = str(self.activity).ljust(45) # Activity
    partD = str(self.product).ljust(35)  # Product
    hours = str(self.hours).ljust(5)
    ltd   = str(self.workType).ljust(10)
    logging.debug(str(date) + '|' + partA + '|' + partB + '|' + partC + '|' + partD + '|' + hours + '|' + ltd)

#-----------------------------------------------------------------------
# Class Timesheet
#-----------------------------------------------------------------------
class Timesheet:
  def __init__(self, ssdata, wsDate):
    self.entries = []
    self.ssdata  = ssdata
    self.wsDate  = wsDate

  #---------------------------------------------------------------------
  def calcDate(self,day):
    day = day.lower().strip()
    day = day[0:3]
    day = { 'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6 }.get(day,7)
    if (day == 7):
      logging.error('Invalid Day')
    date = self.wsDate + datetime.timedelta(days = day)
    return date

  #---------------------------------------------------------------------
  def Clean(self):
    for i,entry in enumerate(self.entries):
      entry.Log()

  #---------------------------------------------------------------------
  def ReadFile(self):
    path = self.ssdata.filename
    logging.debug(path)
    wb = load_workbook(path)
    sheet_names = wb.get_sheet_names();
    if (sheet_names[0] != 'Timesheet'):
      logging.error(path + ' is not a valid Timesheet spreadsheet')

    ws = wb.get_sheet_by_name('Timesheet')

    wsRow     = 7
    wsCol     = 4
    sundayFlg = False
    sundayCnt = 0;
    blankFlg  = False
    curDate   = None

    if (ws.cell(row=6,column=4).value == 'Customer - Part A'): 
      wsCol = 3
    elif (ws.cell(row=6,column=5).value == 'Customer - Part A'):
      wsCol = 4
    else:
      logging.error('Couldn\'t sync to Timesheet spreadsheet')
      return

    while True:
      day = ws.cell(row=wsRow,column=wsCol+0).value
      if (day == None):
        day = ''
        if (curDate == None):
          logging.error('SHOULDNT BE HERE')
      else:
        curDate = self.calcDate(day)
 
      partA  = ws.cell(row=wsRow,column=wsCol+1).value
      if (partA == None):
        partA = ''
        blankFlg = True

      partB = ws.cell(row=wsRow,column=wsCol+2).value
      if (partB == None):
        partB = ''

      partC = ws.cell(row=wsRow,column=wsCol+3).value
      if (partC == None):
        partC = ''

      partD = ws.cell(row=wsRow,column=wsCol+4).value
      if (partD == None):
        partD = ''

      hours = ws.cell(row=wsRow,column=wsCol+9).value
      if (hours == None):
        hours = ''
      else:
        try:
          hours = float(hours)
        except:
          hours = ''

      ltd = ws.cell(row=wsRow,column=wsCol+10).value
      if (ltd == None):
        ltd = ''

      notes = ws.cell(row=wsRow,column=wsCol+11).value
      if (notes == None):
        notes = ''
 
      # TODO: if blankFlg == False, then make sure everything else is blank

      if (not blankFlg):
        self.entries.append(TSEntry(curDate,partA,partB,partC,partD,hours,ltd,notes))

      if (day.startswith('Sunday')):
        sundayFlg = True
      if (sundayFlg):
        if (blankFlg):
          sundayCnt += 1
        else:
          sundayCnt = 0;
      if (sundayCnt > 5):
        break

      wsRow += 1
      blankFlg = False

  #---------------------------------------------------------------------
  def Log(self):
    for i,entry in enumerate(self.entries):
      fullname = self.ssdata.fae.fullname.ljust(25)
      date  = str(self.entries[i].date)
      partA = str(self.entries[i].code).ljust(50)
      partB = str(self.entries[i].location).ljust(60)
      partC = str(self.entries[i].activity).ljust(45)
      partD = str(self.entries[i].product).ljust(35)
      hours = str(self.entries[i].hours).ljust(5)
      ltd   = str(self.entries[i].worktype).ljust(10)
      logging.debug(fullname + '|' + str(date) + '|' + partA + '|' + partB + '|' + partC + '|' + partD + '|' + hours + '|' + ltd)

