import os
import os.path
import datetime
import logging
from   Calendar import Calendar
from   FAE      import FAETeam

finished = []

def GetFiles(root):
  list = []
  walk(root, list)
  return list

def walk(rootdir, list):
  for curdir, subdirs, files in os.walk(rootdir):
    for file in files:
      if (file.startswith('Timesheet')):
        fname = os.path.join(rootdir,file)
        list.append(fname)
    if (subdirs):
      for subdir in subdirs:
        dir = os.path.join(rootdir,subdir)
        walk(dir, list)
    break

#-----------------------------------------------------------------------
class FLDate:
  def __init__(self,date):
    self.asStr = str(date)
    self.asDate = date

  def GetWSVal(self):
    if (len(self.asStr) == 0):
      return None
    else:
      return self.asStr

#-----------------------------------------------------------------------
class FLFile:
  def __init__(self,filename):
    self.fae      = None
    self.fname    = None
    self.lname    = None
    self.fullname = None
    self.filename = None
    self.weDate   = None
    self.wsDate   = None
    self.valid    = False

    filenameinfo = os.path.basename(filename).split();
    if (len(filenameinfo) != 7):
      return

    year  = int(filenameinfo[6][0:4])
    if (year < 2016 or year > 2020): 
      return
    month = int(filenameinfo[6][5:7])
    if (month < 1 or month > 12): 
      return
    day   = int(filenameinfo[6][8:10])
    if (day < 1 or day > 31): 
      return

    weDate = datetime.date(year, month, day)
    if (weDate not in Calendar.weDates):
      return
    wsDate = weDate - datetime.timedelta(days=6)

    self.fname    = filenameinfo[2]
    self.lname    = filenameinfo[3]
    self.fullname = self.fname + ' ' + self.lname
    if (self.fullname not in FAETeam.dict):
      return

    self.filename = filename
    self.weDate   = FLDate(weDate)
    self.wsDate   = FLDate(wsDate)
    self.valid    = True

  def __lt__(self,other): 
    if (str(self.fae.team) != str(other.fae.team)):
      if (str(self.fae.team) < str(other.fae.team)):
        return True
      else:
        return False
    elif (str(self.fae.loc) != str(other.fae.loc)):
      if (str(self.fae.loc) < str(other.fae.loc)):
        return True
      else:
        return False
    elif (str(self.fae.lname) != str(other.fae.lname)):
      if (str(self.fae.lname) < str(other.fae.lname)):
        return True
      else:
        return False
    elif (str(self.fae.fname) != str(other.fae.fname)):
      if (str(self.fae.fname) < str(other.fae.fname)):
        return True
      else:
        return False
    logging.error('SHOULD NOT BE HERE')
    return False
  def __le__(self,other): 
    return True
  def __gt__(self,other): 
    return True
  def __ge__(self,other): 
    return True
  def __eq__(self,other): 
    return True
  def __ne__(self,other): 
    return True

  def AddFAE(self,fae):
    self.fae = fae

  def IsValid(self):
    return (self.valid == True and self.fae != None)

  def Log(self):
    pass
    #logging.debug(str(self.wsDate) + ' ' + self.fname + ' ' + self.lname)

#-----------------------------------------------------------------------
class FLData:
  def __init__(self):
    self.weeks = {}

  def AddFile(self,tsfile):
    date = tsfile.wsDate.asDate
    if (date not in self.weeks):
      self.weeks[date] = {}
    name = tsfile.fullname
    if (name not in self.weeks[date]):
      self.weeks[date][name] = tsfile
    else:
      logging.error('Timesheet already exists for ' + str(date) + ' ' + name)

  def Validate(self):
    for date in self.weeks:
      cnt = 0
      for name in FAETeam.dict:
        if (name not in self.weeks[date]):
          logging.error('Missing Timesheet for week starting ' + str(date) + ' ' + name)
        else:
          cnt += 1
      #logging.debug('Week ' + str(date) + ' Cnt ' + str(cnt))

  def Log(self):
    pass
    #for week in self.weeks:
    #  logging.debug('Week' + ' ' + str(week))
    #  for name in self.weeks[week]:
    #    logging.debug('Name' + '            ' + name)


