import os
import datetime
import logging

#-----------------------------------------------------------------------
class TSFile:
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

#-----------------------------------------------------------------------
class TSData:
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
      logging.debug('Week ' + str(date) + ' Cnt ' + str(cnt))

  def Log(self):
    for week in self.weeks:
      logging.debug('Week' + ' ' + str(week))
      for name in self.weeks[week]:
        logging.debug('Name' + '            ' + name)


#-----------------------------------------------------------------------
class Week:
  def __init__(self):
    self.date = None
    self.tsinfo = []

#-----------------------------------------------------------------------
#class TSInfo:
#  def __init__(self,fnameinfo):
#    self.fname    = fnameinfo.fname
#    self.lname    = fnameinfo.lname
#    self.fullname = fnameinfo.fullname
#    self.filename = fnameinfo.filename
#    self.weDate   = fnameinfo.weDate
#    self.wsDate   = fnameinfo.wsDate
#    self.valid    = True
#
#  def Log(self):
#    logging.debug(str(self.wsDate) + ' ' + self.fname + ' ' + self.lname)

#-----------------------------------------------------------------------
class FAEMember:
  def __init__(self,fname,lname,laborType,team,loc):
    self.fname     = fname
    self.lname     = lname
    self.fullname  = fname + ' ' + lname
    self.laborType = laborType
    self.team      = team
    self.loc       = loc

class FAETeam:
  def __init__(self):
    self.members = {}
    self.members['Wray Odom'         ] = FAEMember('Wray'    ,'Odom'      ,'P','DMR','E')
    self.members['Pankaj Wadhwa'     ] = FAEMember('Pankaj'  ,'Wadhwa'    ,'C','DMR','E')
    self.members['Andy Cooper'       ] = FAEMember('Andy'    ,'Cooper'    ,'P','DMR','E')
    self.members['Kapil Bhardwaj'    ] = FAEMember('Kapil'   ,'Bhardwaj'  ,'P','DMR','E')
    self.members['Sohan D\'Souza'    ] = FAEMember('Sohan'   ,'D\'Souza'  ,'P','DMR','E')
    self.members['Jeremy Schroeder'  ] = FAEMember('Jeremy'  ,'Schroder'  ,'P','DMR','E')
    self.members['Emad Ramahi'       ] = FAEMember('Emad'    ,'Ramahi'    ,'P','DMR','E')
    self.members['Karun Dua'         ] = FAEMember('Karun'   ,'Dua'       ,'P','DMR','W')
    self.members['Suarabh Dhancholia'] = FAEMember('Suarabh' ,'Dhancholia','P','DMR','W')
    self.members['Jeff Smith'        ] = FAEMember('Jeff'    ,'Smith'     ,'P','DMR','W')
    self.members['Paul Khatkar'      ] = FAEMember('Paul'    ,'Khatkar'   ,'P','DMR','W')
    self.members['Joel Joseph'       ] = FAEMember('Joel'    ,'Joseph'    ,'P','DMR','W')
    self.members['Ashwini Bhagat'    ] = FAEMember('Ashwini' ,'Bhagat'    ,'P','DMR','W')
    self.members['Jim Morrison'      ] = FAEMember('Jim'     ,'Morrison'  ,'P','MI' ,'R')
    self.members['Paul Moser'        ] = FAEMember('Paul'    ,'Moser'     ,'P','MI' ,'R')
    self.members['Karl Hornung'      ] = FAEMember('Karl'    ,'Hornung'   ,'P','MI' ,'R')
    self.members['Jonathan Smith'    ] = FAEMember('Jonathan','Smith'     ,'P','MI' ,'R')
    self.members['Pouyan Rostam'     ] = FAEMember('Pouyan'  ,'Rostam'    ,'C','DMR','C')
    self.members['Karan Kalsi'       ] = FAEMember('Karan'   ,'Kalsi'     ,'C','DMR','C')
    self.members['Pallavi Chaturvedi'] = FAEMember('Pallavi' ,'Chaturvedi','C','DMR','C')



  def Append(self, fae):
    self.members.append(fae)

class RegionReport:
  def __init__(self):
    self.list = []

class TSCalendar:
  def __init__(self,year):
    d = datetime.date(year,1,1)
    while (True):
      logging.debug(d.weekday())
      if (d.weekday() == 0):
        break;
      else:
        d = d + datetime.timedelta(days=1)
    logging.debug(d)
    week = {}
    i = 1
    while(True):
      week[i] = d
      logging.debug(str(i) + ' ' + str(week[i]))
      d = d + datetime.timedelta(days = 7)
      if (d.year > year):
        break;
      i += 1
    logging.debug(week)
 



class TSSummary:
  def __init__(self):
    self.list = []

  def Process(self,tsdata,team,root):
    pass






