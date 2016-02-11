import os
import datetime
import logging

#-----------------------------------------------------------------------
class FAEMember:
  def __init__(self,fname,lname,laborType,team,loc):
    self.fname     = fname
    self.lname     = lname
    self.fullname  = fname + ' ' + lname
    self.laborType = laborType
    self.team      = team
    self.loc       = loc

#-----------------------------------------------------------------------
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

#-----------------------------------------------------------------------
class TSFile:
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

    #check day of week; should be mon and sun

  #def __repr__(self):
  #  return '{}: {} {}'.format(self.__class__.__name__,self.wsDate,self.fullname)

  #def TSFileCompare(x,y):
  #  if (self.fae.team < other.fae.team): return other
  #  if (self.fae.team == other.fae.team):
  #    if (self.fae.loc < other.fae.loc):return other
  #  if (self.lname < other.lname): return other
  #  if (self.lname == other.lname):
  #    if (self.fname < other.fname): return other
  #  return self

  def __lt__(self,other): 
    #logging.debug(self.fae.team + ' ' + self.fae.loc + ' ' + self.fae.fullname + ' - ' + other.fae.team + ' ' + other.fae.loc + ' ' + other.fae.fullname)
    if (self.fae.team != other.fae.team):
      if (self.fae.team < other.fae.team):
        #logging.debug(self.fae.team + ' is LT')
        return True
      else:
        return False
    elif (self.fae.loc != other.fae.loc):
      if (self.fae.loc < other.fae.loc):
        #logging.debug(self.fae.loc + ' is LT')
        return True
      else:
        return False
    elif (self.fae.lname != other.fae.lname):
      if (self.fae.lname < other.fae.lname):
        #logging.debug(self.fae.lname + ' is LT')
        return True
      else:
        return False
    elif (self.fae.fname != other.fae.fname):
      if (self.fae.fname < other.fae.fname):
        #logging.debug(self.fae.fname + ' is LT')
        return True
      else:
        return False
    logging.error('SHOULD NOT BE HERE')
    return False
    #if (self.fae.team  < other.fae.team):
    #  logging.debug(self.fae.team + ' is LT') 
    #  return True
    #elif (self.fae.loc < other.fae.loc):
    #  logging.debug(self.fae.loc + ' is LT')
    #  return True
    #elif (self.fae.lname < other.fae.lname):
    #  logging.debug(self.fae.lname + ' is LT')
    #  return True
    #elif (self.fae.fname < other.fae.fname):
    #  logging.debug(self.fae.fname + ' is LT') 
    #  return True
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


class RegionReport:
  def __init__(self):
    self.week = {}

class TSCalendar:
  def __init__(self,year):
    self.week = {}
    d = datetime.date(year,1,1)
    while (True):
      #logging.debug(d.weekday())
      if (d.weekday() == 0):
        break;
      else:
        d = d + datetime.timedelta(days=1)
    #logging.debug(d)
    i = 1
    while(True):
      self.week[i] = d
      #logging.debug(str(i) + ' ' + str(self.week[i]))
      d = d + datetime.timedelta(days = 7)
      if (d.year > year):
        break;
      i += 1
   
  def Log(self):
    cnt = len(self.week)
    for i in range(1,cnt+1):
      logging.debug(str(i) + ' ' + str(self.week[i])) 
 



class TSSummary:
  def __init__(self):
    self.sslist = []


  def Process(self,tsdata,team,year,week):
    cal = TSCalendar(year)
    self.Sort(tsdata,cal,week)

  def Sort(self,tsdata,cal,week):
    self.sslist = []
    for i in range(1,week+1):
      list = []
      dict = {}
      logging.debug(str(i) + ' ' + str(cal.week[i]))
      dict = tsdata.weeks[cal.week[i]]
      for key,value in dict.items():
        list.append(value)
      self.sslist.append(sorted(list))
      #list.sort(key=list.Compare)
      #for j in list:
      #  logging.debug(j.fae.team + ' ' + j.fae.loc + ' ' + j.fae.fullname)
 
    for i,week in enumerate(self.sslist):
      logging.debug(cal.week[i+1])
      for j,item in enumerate(week):
        logging.debug(item.fae.team + ' ' + item.fae.loc + ' ' + item.fae.fullname)
    #for i in range(len(self.sslist)):
    #  logging.debug(cal.week[k])
    #  for j in range(len(self.sslist[i])):
    #    logging.debug(j.fae.team + ' ' + j.fae.loc + ' ' + j.fae.fullname)
    #  k += 1
        

    logging.debug('sorted list')






