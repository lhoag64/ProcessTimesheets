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

#-----------------------------------------------------------------------
class FAETeam:
  dict = None
  list = None

  def Init():
    FAETeam.dict = {}
    FAETeam.list  = []

    FAETeam.dict['Alex Blackwood'    ] = FAEMember('Alex'   ,'Blackwood'   ,'P','DMR','UK','2014-01-01','2020-01-01')
    FAETeam.dict['Piyush Agarwal'    ] = FAEMember('Piyush' ,'Agarwal'     ,'P','DMR','UK','2014-01-01','2020-01-01')
    FAETeam.dict['Jawid Azizi'       ] = FAEMember('Jawid'  ,'Azizi'       ,'P','DMR','UK','2014-01-01','2020-01-01')
    FAETeam.dict['Chu Qi Yau'        ] = FAEMember('Chu'    ,'Qi Yau'      ,'P','DMR','UK','2014-01-01','2020-01-01')
    FAETeam.dict['Ashok Yadav'       ] = FAEMember('Ashok'  ,'Yadav'       ,'C','DMR','UK','2014-01-01','2020-01-01')
    FAETeam.dict['Haroon Azizi'      ] = FAEMember('Haroon' ,'Azizi'       ,'P','DMR','UK','2014-01-01','2020-01-01')
    FAETeam.dict['Tomas Helge'       ] = FAEMember('Tomas'  ,'Helge'       ,'C','DMR','SE','2014-01-01','2020-01-01')
    FAETeam.dict['Farshid Saidbahr'  ] = FAEMember('Farshid','Saidbahr'    ,'P','DMR','SE','2014-01-01','2020-01-01')
    FAETeam.dict['Stefan Edblom'     ] = FAEMember('Stefan' ,'Edblom'      ,'C','DMR','SE','2014-01-01','2020-01-01')
    FAETeam.dict['Rajesh Kallingal'  ] = FAEMember('Rajesh' ,'Kallingal'   ,'C','DMR','SE','2014-01-01','2020-01-01')
    FAETeam.dict['Akash Jha'         ] = FAEMember('Akash'  ,'Jha'         ,'C','DMR','SE','2014-01-01','2020-01-01')
    FAETeam.dict['Joakim Marjeta'    ] = FAEMember('Joakim' ,'Marjeta'     ,'P','DMR','FI','2014-01-01','2020-01-01')
    FAETeam.dict['Kai Hietala'       ] = FAEMember('Kai'    ,'Hietala'     ,'P','DMR','FI','2014-01-01','2020-01-01')
    FAETeam.dict['Jouni Keski-Santti'] = FAEMember('Jouni'  ,'Keski-Santti','C','DMR','FI','2016-07-07','2020-01-01')
    FAETeam.dict['Kamal Mudgal'      ] = FAEMember('Kamal'  ,'Mudgal'      ,'C','DMR','FR','2014-01-01','2020-01-01')
    FAETeam.dict['Germain Irankunda' ] = FAEMember('Germain','Irankunda'   ,'C','DMR','FR','2014-01-01','2020-01-01')
    FAETeam.dict['Marco Hofbeck'     ] = FAEMember('Marco'  ,'Hofbeck'     ,'P','DMR','DE','2014-01-01','2020-01-01')

    FAETeam.list = sorted(FAETeam.dict.values())

#    for fae in FAETeam.list:
#      logging.debug(str(fae.team).ljust(3) + ' ' + str(fae.loc) + ' ' + str(fae.lname).ljust(12))

#  def Append(self, fae):
#    self.members.append(fae)






