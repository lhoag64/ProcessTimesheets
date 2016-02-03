import os
import datetime
import logging

class TSFileNameInfo:
  def __init__(self,filename):
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

    #check day of week; should be mon and sun

  def __repr__(self):
    return '{}: {} {}'.format(self.__class__.__name__,self.wsDate,self.fullname)

  def IsValid(self):
    return self.valid

  def Log(self):
    logging.debug(str(self.wsDate) + ' ' + self.fname + ' ' + self.lname)


class Week:
  def __init__(self):
    self.list = []

class FAEMember:
  def __init__(self):
    self.list = []

class FAETeam:
  def __init__(self):
    self.list = []

class RegionReport:
  def __init__(self):
    self.list = []








