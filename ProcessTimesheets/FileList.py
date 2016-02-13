import os
import os.path
import datetime
import logging

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
class FLFile:
  def __init__(self,filename):
    self.fae   = None
    self.valid = False
    filenameinfo = os.path.basename(filename).split();
    if (len(filenameinfo) != 7):
      return

    year  = int(filenameinfo[6][0:4])
    if (year < 2016 or year > 2020): return
    month = int(filenameinfo[6][5:7])
    if (month < 1 or month > 12): return
    day   = int(filenameinfo[6][8:10])
    if (day < 1 or day > 31): return

    self.fname    = filenameinfo[2]
    self.lname    = filenameinfo[3]
    self.fullname = self.fname + ' ' + self.lname
    self.filename = filename
    self.weDate   = datetime.date(year, month, day)
    self.wsDate   = self.weDate - datetime.timedelta(days=6)
    self.valid    = True

  def __lt__(self,other): 
    if (self.fae.team != other.fae.team):
      if (self.fae.team < other.fae.team):
        return True
      else:
        return False
    elif (self.fae.loc != other.fae.loc):
      if (self.fae.loc < other.fae.loc):
        return True
      else:
        return False
    elif (self.fae.lname != other.fae.lname):
      if (self.fae.lname < other.fae.lname):
        return True
      else:
        return False
    elif (self.fae.fname != other.fae.fname):
      if (self.fae.fname < other.fae.fname):
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
    date = tsfile.wsDate
    if (date not in self.weeks):
      self.weeks[date] = {}
    name = tsfile.fullname
    if (name not in self.weeks[date]):
      self.weeks[date][name] = tsfile
    else:
      logging.error('Timesheet already exists for ' + str(date) + ' ' + name)

  def Validate(self, faes):
    for date in self.weeks:
      cnt = 0
      for name in faes.members:
        if (name not in self.weeks[date]):
          logging.error('Missing Timesheet for ' + str(date) + ' ' + name)
        else:
          cnt += 1
      #logging.debug('Week ' + str(date) + ' Cnt ' + str(cnt))

  def Log(self):
    pass
    #for week in self.weeks:
    #  logging.debug('Week' + ' ' + str(week))
    #  for name in self.weeks[week]:
    #    logging.debug('Name' + '            ' + name)


