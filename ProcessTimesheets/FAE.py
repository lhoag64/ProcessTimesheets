#import os
#import datetime
import logging
#from openpyxl import load_workbook

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






