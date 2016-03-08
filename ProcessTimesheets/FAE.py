#import os
import datetime
import logging
#from openpyxl import load_workbook

#-----------------------------------------------------------------------
class FAEName:
  def __init__(self,name):
    self.asStr = name

  def GetWSVal(self): return self.asStr
  def GetVal(self): return self.asStr
  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class FAEDate:
  def __init__(self,date):
    self.asStr = date
    year = int(date[0:4])
    mon  = int(date[5:7])
    day  = int(date[8:10])
    self.asDate = datetime.date(year,mon,day)

  def GetWSVal(self): return self.asStr
  def GetStr(self): return self.asDate
  def GetVal(self): return self.asDate
  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class FAELaborType:
  def __init__(self,lType):
    self.asStr = lType

  def GetWSVal(self): return self.asStr
  def GetVal(self): return self.asStr
  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class FAETeamType:
  def __init__(self,team):
    self.asStr = team

  def GetWSVal(self): return self.asStr
  def GetVal(self): return self.asStr
  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class FAELocation:
  def __init__(self,loc):
    self.asStr = loc

  def GetWSVal(self): return self.asStr
  def GetVal(self): return self.asStr
  def __str__(self): return self.asStr

#-----------------------------------------------------------------------
class FAEMember:
  def __init__(self,fname,lname,laborType,team,loc,sDate,eDate):
    self.fname     = FAEName(fname)
    self.lname     = FAEName(lname)
    self.fullname  = FAEName(fname + ' ' + lname)
    self.laborType = FAELaborType(laborType)
    self.team      = FAETeamType(team)
    self.loc       = FAELocation(loc)
    self.startDate = FAEDate(sDate)
    self.endDate   = FAEDate(eDate)

  def __lt__(self,other):
    if (str(self.team) != str(other.team)):
      if (str(self.team) < str(other.team)):
        return True
      else:
        return False
    elif (str(self.loc) != str(other.loc)):
      if (str(self.loc) < str(other.loc)):
        return True
      else:
        return False
    elif (str(self.lname) != str(other.lname)):
      if (str(self.lname) < str(other.lname)):
        return True
      else:
        return False
    elif (str(self.fname) != str(other.fname)):
      if (str(self.fname) < str(other.fname)):
        return True
      else:
        return False
    logging.error('SHOULD NOT BE HERE')
    return False




