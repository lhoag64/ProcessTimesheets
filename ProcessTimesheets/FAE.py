#import os
#import datetime
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
  def __init__(self,name):
    self.asStr = name

  def GetWSVal(self): return self.asStr
  def GetVal(self): return self.asStr
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
    FAETeam.dict['Wray Odom'         ] = FAEMember('Wray'    ,'Odom'      ,'P','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Pankaj Wadhwa'     ] = FAEMember('Pankaj'  ,'Wadhwa'    ,'C','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Andy Cooper'       ] = FAEMember('Andy'    ,'Cooper'    ,'P','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Kapil Bhardwaj'    ] = FAEMember('Kapil'   ,'Bhardwaj'  ,'P','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Sohan D\'souza'    ] = FAEMember('Sohan'   ,'D\'souza'  ,'P','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Jeremy Schroeder'  ] = FAEMember('Jeremy'  ,'Schroeder' ,'P','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Emad Ramahi'       ] = FAEMember('Emad'    ,'Ramahi'    ,'P','DMR','E','2014-01-01','2020-01-01')
    FAETeam.dict['Karun Dua'         ] = FAEMember('Karun'   ,'Dua'       ,'P','DMR','W','2014-01-01','2020-01-01')
    FAETeam.dict['Suarabh Dhancholia'] = FAEMember('Suarabh' ,'Dhancholia','P','DMR','W','2014-01-01','2020-01-01')
    FAETeam.dict['Jeff Smith'        ] = FAEMember('Jeff'    ,'Smith'     ,'P','DMR','W','2014-01-01','2016-02-05')
    FAETeam.dict['Paul Khatkar'      ] = FAEMember('Paul'    ,'Khatkar'   ,'P','DMR','W','2014-01-01','2020-01-01')
    FAETeam.dict['Joel Joseph'       ] = FAEMember('Joel'    ,'Joseph'    ,'P','DMR','W','2014-01-01','2020-01-01')
    FAETeam.dict['Ashwini Bhagat'    ] = FAEMember('Ashwini' ,'Bhagat'    ,'P','DMR','W','2014-01-01','2020-01-01')
    FAETeam.dict['Jim Morrison'      ] = FAEMember('Jim'     ,'Morrison'  ,'P','MI' ,'R','2014-01-01','2020-01-01')
    FAETeam.dict['Paul Moser'        ] = FAEMember('Paul'    ,'Moser'     ,'P','MI' ,'R','2014-01-01','2020-01-01')
    FAETeam.dict['Karl Hornung'      ] = FAEMember('Karl'    ,'Hornung'   ,'P','MI' ,'R','2014-01-01','2020-01-01')
    FAETeam.dict['Jonathan Smith'    ] = FAEMember('Jonathan','Smith'     ,'P','MI' ,'R','2014-01-01','2020-01-01')
    FAETeam.dict['Pouyan Rostam'     ] = FAEMember('Pouyan'  ,'Rostam'    ,'C','DMR','C','2014-01-01','2016-01-15')
    FAETeam.dict['Karan Kalsi'       ] = FAEMember('Karan'   ,'Kalsi'     ,'C','DMR','C','2014-01-01','2020-01-01')
    FAETeam.dict['Pallavi Chaturvedi'] = FAEMember('Pallavi' ,'Chaturvedi','C','DMR','C','2014-01-01','2020-01-01')

    FAETeam.list = sorted(FAETeam.dict.values())

#    for fae in FAETeam.list:
#      logging.debug(str(fae.team).ljust(3) + ' ' + str(fae.loc) + ' ' + str(fae.lname).ljust(12))

#  def Append(self, fae):
#    self.members.append(fae)






