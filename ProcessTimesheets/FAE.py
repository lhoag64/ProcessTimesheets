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

    FAETeam.dict['Eric Liu'     ] = FAEMember('Eric'   ,'Liu'   ,'P','DMR','N','2014-01-01','2020-01-01')
    FAETeam.dict['Young Wang'   ] = FAEMember('Young'  ,'Wang'  ,'P','DMR','N','2014-01-01','2020-01-01')
    FAETeam.dict['Ronald Luan'  ] = FAEMember('Ronald' ,'Luan'  ,'P','DMR','N','2014-01-01','2020-01-01')
    FAETeam.dict['Yukang Tu'    ] = FAEMember('Yukang' ,'Tu'    ,'P','DMR','N','2014-01-01','2020-01-01')
    FAETeam.dict['Wayne Fu'     ] = FAEMember('Wayne'  ,'Fu'    ,'P','DMR','N','2014-01-01','2020-01-01')
    FAETeam.dict['Mark Yan'     ] = FAEMember('Mark'   ,'Yan'   ,'P','DMR','N','2014-01-01','2020-01-01')
    FAETeam.dict['Klein Jiang'  ] = FAEMember('Klein'  ,'Jiang' ,'P','DMR','S','2014-01-01','2020-01-01')
    FAETeam.dict['Corey Liu'    ] = FAEMember('Corey'  ,'Liu'   ,'P','DMR','S','2014-01-01','2020-01-01')
    FAETeam.dict['Huang Wei'    ] = FAEMember('Huang'  ,'Wei'   ,'P','DMR','S','2014-01-01','2020-01-01')
    FAETeam.dict['Wang Sining'  ] = FAEMember('Wang'   ,'Sining','P','DMR','S','2014-01-01','2020-01-01')
    FAETeam.dict['Iblic Lin'    ] = FAEMember('Iblic'  ,'Lin'   ,'P','DMR','S','2014-01-01','2020-01-01')
    FAETeam.dict['Tiger Chen'   ] = FAEMember('Tiger'  ,'Chen'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['Huang Zheer'  ] = FAEMember('Huang'  ,'Zheer' ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['Gary Wang'    ] = FAEMember('Gary'   ,'Wang'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['David Wang'   ] = FAEMember('David'  ,'Wang'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['Chien Huang'  ] = FAEMember('Chien'  ,'Huang' ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['Hu Yu'        ] = FAEMember('Hu'     ,'Yu'    ,'P','MI' ,'N','2014-01-01','2020-01-01')
    FAETeam.dict['Eric Wang'    ] = FAEMember('Eric'   ,'Wang'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['Kowski Heieh' ] = FAEMember('Kowski' ,'Heieh' ,'P','MI' ,'S','2014-01-01','2020-01-01')
    FAETeam.dict['Jun Yang'     ] = FAEMember('Jun'    ,'Yang'  ,'P','TVM','N','2014-01-01','2020-01-01')
    FAETeam.dict['Michael Zhang'] = FAEMember('Michael','Zhang' ,'P','TVM','S','2014-01-01','2020-01-01')
    FAETeam.dict['Simon Liu'    ] = FAEMember('Simon'  ,'Liu'   ,'P','DAS','N','2014-01-01','2020-01-01')
    FAETeam.dict['Ray Zhang'    ] = FAEMember('Ray'    ,'Zhang' ,'P','DAS','N','2014-01-01','2020-01-01')
    FAETeam.dict['Zhao Jing'    ] = FAEMember('Zhao'   ,'Jing'  ,'P','DAS','N','2014-01-01','2016-02-01')

    FAETeam.list = sorted(FAETeam.dict.values())

#    for fae in FAETeam.list:
#      logging.debug(str(fae.team).ljust(3) + ' ' + str(fae.loc) + ' ' + str(fae.lname).ljust(12))

#  def Append(self, fae):
#    self.members.append(fae)






