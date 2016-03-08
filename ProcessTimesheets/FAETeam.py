import datetime
import logging
from FAE import FAEMember

class FAETeam:
  def __init__(self):
    self.dict = None
    self.list = None

class AMTeam(FAETeam):
  def __init__(self):
    self.dict = {}
    self.list = None

    self.dict['Wray Odom'         ] = FAEMember('Wray'    ,'Odom'      ,'P','DMR','E','2014-01-01','2020-01-01')
    self.dict['Pankaj Wadhwa'     ] = FAEMember('Pankaj'  ,'Wadhwa'    ,'C','DMR','E','2014-01-01','2020-01-01')
    self.dict['Andy Cooper'       ] = FAEMember('Andy'    ,'Cooper'    ,'P','DMR','E','2014-01-01','2020-01-01')
    self.dict['Kapil Bhardwaj'    ] = FAEMember('Kapil'   ,'Bhardwaj'  ,'P','DMR','E','2014-01-01','2020-01-01')
    self.dict['Sohan D\'souza'    ] = FAEMember('Sohan'   ,'D\'souza'  ,'P','DMR','E','2014-01-01','2020-01-01')
    self.dict['Jeremy Schroeder'  ] = FAEMember('Jeremy'  ,'Schroeder' ,'P','DMR','E','2014-01-01','2020-01-01')
    self.dict['Emad Ramahi'       ] = FAEMember('Emad'    ,'Ramahi'    ,'P','DMR','E','2014-01-01','2020-01-01')
    self.dict['Karun Dua'         ] = FAEMember('Karun'   ,'Dua'       ,'P','DMR','W','2014-01-01','2020-01-01')
    self.dict['Suarabh Dhancholia'] = FAEMember('Suarabh' ,'Dhancholia','P','DMR','W','2014-01-01','2020-01-01')
    self.dict['Jeff Smith'        ] = FAEMember('Jeff'    ,'Smith'     ,'P','DMR','W','2014-01-01','2016-02-05')
    self.dict['Paul Khatkar'      ] = FAEMember('Paul'    ,'Khatkar'   ,'P','DMR','W','2014-01-01','2020-01-01')
    self.dict['Joel Joseph'       ] = FAEMember('Joel'    ,'Joseph'    ,'P','DMR','W','2014-01-01','2020-01-01')
    self.dict['Ashwini Bhagat'    ] = FAEMember('Ashwini' ,'Bhagat'    ,'P','DMR','W','2014-01-01','2020-01-01')
    self.dict['Jim Morrison'      ] = FAEMember('Jim'     ,'Morrison'  ,'P','MI' ,'R','2014-01-01','2020-01-01')
    self.dict['Paul Moser'        ] = FAEMember('Paul'    ,'Moser'     ,'P','MI' ,'R','2014-01-01','2020-01-01')
    self.dict['Karl Hornung'      ] = FAEMember('Karl'    ,'Hornung'   ,'P','MI' ,'R','2014-01-01','2020-01-01')
    self.dict['Jonathan Smith'    ] = FAEMember('Jonathan','Smith'     ,'P','MI' ,'R','2014-01-01','2020-01-01')
    self.dict['Pouyan Rostam'     ] = FAEMember('Pouyan'  ,'Rostam'    ,'C','DMR','C','2014-01-01','2016-01-15')
    self.dict['Karan Kalsi'       ] = FAEMember('Karan'   ,'Kalsi'     ,'C','DMR','C','2014-01-01','2020-01-01')
    self.dict['Pallavi Chaturvedi'] = FAEMember('Pallavi' ,'Chaturvedi','C','DMR','C','2014-01-01','2020-01-01')

    self.list = sorted(self.dict.values())



#-----------------------------------------------------------------------
class EMEATeam(FAETeam):
  def __init__(self):
    self.dict = {}
    self.list = None

    self.dict['Alex Blackwood'    ] = FAEMember('Alex'   ,'Blackwood'   ,'P','DMR','UK','2014-01-01','2020-01-01')
    self.dict['Piyush Agarwal'    ] = FAEMember('Piyush' ,'Agarwal'     ,'P','DMR','UK','2014-01-01','2020-01-01')
    self.dict['Jawid Azizi'       ] = FAEMember('Jawid'  ,'Azizi'       ,'P','DMR','UK','2014-01-01','2020-01-01')
    self.dict['Chu Qi Yau'        ] = FAEMember('Chu'    ,'Qi Yau'      ,'P','DMR','UK','2014-01-01','2020-01-01')
    self.dict['Ashok Yadav'       ] = FAEMember('Ashok'  ,'Yadav'       ,'C','DMR','UK','2014-01-01','2020-01-01')
    self.dict['Haroon Azizi'      ] = FAEMember('Haroon' ,'Azizi'       ,'P','DMR','UK','2014-01-01','2020-01-01')
    self.dict['Tomas Helge'       ] = FAEMember('Tomas'  ,'Helge'       ,'C','DMR','SE','2014-01-01','2020-01-01')
    self.dict['Farshid Saidbahr'  ] = FAEMember('Farshid','Saidbahr'    ,'P','DMR','SE','2014-01-01','2020-01-01')
    self.dict['Stefan Edblom'     ] = FAEMember('Stefan' ,'Edblom'      ,'C','DMR','SE','2014-01-01','2020-01-01')
    self.dict['Rajesh Kallingal'  ] = FAEMember('Rajesh' ,'Kallingal'   ,'C','DMR','SE','2014-01-01','2020-01-01')
    self.dict['Akash Jha'         ] = FAEMember('Akash'  ,'Jha'         ,'C','DMR','SE','2014-01-01','2020-01-01')
    self.dict['Joakim Marjeta'    ] = FAEMember('Joakim' ,'Marjeta'     ,'P','DMR','FI','2014-01-01','2020-01-01')
    self.dict['Kai Hietala'       ] = FAEMember('Kai'    ,'Hietala'     ,'P','DMR','FI','2014-01-01','2020-01-01')
    self.dict['Jouni Keski-Santti'] = FAEMember('Jouni'  ,'Keski-Santti','C','DMR','FI','2016-07-07','2020-01-01')
    self.dict['Kamal Mudgal'      ] = FAEMember('Kamal'  ,'Mudgal'      ,'C','DMR','FR','2014-01-01','2020-01-01')
    self.dict['Germain Irankunda' ] = FAEMember('Germain','Irankunda'   ,'C','DMR','FR','2014-01-01','2020-01-01')
    self.dict['Marco Hofbeck'     ] = FAEMember('Marco'  ,'Hofbeck'     ,'P','DMR','DE','2014-01-01','2020-01-01')

    self.list = sorted(self.dict.values())


#-----------------------------------------------------------------------
class GCTeam(FAETeam):
  def __init__(self):
    self.dict = {}
    self.list = None

    self.dict['Eric Liu'     ] = FAEMember('Eric'   ,'Liu'   ,'P','DMR','N','2014-01-01','2020-01-01')
    self.dict['Young Wang'   ] = FAEMember('Young'  ,'Wang'  ,'P','DMR','N','2014-01-01','2020-01-01')
    self.dict['Ronald Luan'  ] = FAEMember('Ronald' ,'Luan'  ,'P','DMR','N','2014-01-01','2020-01-01')
    self.dict['Yukang Tu'    ] = FAEMember('Yukang' ,'Tu'    ,'P','DMR','N','2014-01-01','2020-01-01')
    self.dict['Wayne Fu'     ] = FAEMember('Wayne'  ,'Fu'    ,'P','DMR','N','2014-01-01','2020-01-01')
    self.dict['Mark Yan'     ] = FAEMember('Mark'   ,'Yan'   ,'P','DMR','N','2014-01-01','2020-01-01')
    self.dict['Klein Jiang'  ] = FAEMember('Klein'  ,'Jiang' ,'P','DMR','S','2014-01-01','2020-01-01')
    self.dict['Corey Liu'    ] = FAEMember('Corey'  ,'Liu'   ,'P','DMR','S','2014-01-01','2020-01-01')
    self.dict['Huang Wei'    ] = FAEMember('Huang'  ,'Wei'   ,'P','DMR','S','2014-01-01','2020-01-01')
    self.dict['Wang Sining'  ] = FAEMember('Wang'   ,'Sining','P','DMR','S','2014-01-01','2020-01-01')
    self.dict['Iblic Lin'    ] = FAEMember('Iblic'  ,'Lin'   ,'P','DMR','S','2014-01-01','2020-01-01')
    self.dict['Tiger Chen'   ] = FAEMember('Tiger'  ,'Chen'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['Huang Zheer'  ] = FAEMember('Huang'  ,'Zheer' ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['Gary Wang'    ] = FAEMember('Gary'   ,'Wang'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['David Wang'   ] = FAEMember('David'  ,'Wang'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['Chien Huang'  ] = FAEMember('Chien'  ,'Huang' ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['Hu Yu'        ] = FAEMember('Hu'     ,'Yu'    ,'P','MI' ,'N','2014-01-01','2020-01-01')
    self.dict['Eric Wang'    ] = FAEMember('Eric'   ,'Wang'  ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['Kowski Heieh' ] = FAEMember('Kowski' ,'Heieh' ,'P','MI' ,'S','2014-01-01','2020-01-01')
    self.dict['Jun Yang'     ] = FAEMember('Jun'    ,'Yang'  ,'P','TVM','N','2014-01-01','2020-01-01')
    self.dict['Michael Zhang'] = FAEMember('Michael','Zhang' ,'P','TVM','S','2014-01-01','2020-01-01')
    self.dict['Simon Liu'    ] = FAEMember('Simon'  ,'Liu'   ,'P','DAS','N','2014-01-01','2020-01-01')
    self.dict['Ray Zhang'    ] = FAEMember('Ray'    ,'Zhang' ,'P','DAS','N','2014-01-01','2020-01-01')
    self.dict['Zhao Jing'    ] = FAEMember('Zhao'   ,'Jing'  ,'P','DAS','N','2014-01-01','2016-02-01')

    self.list = sorted(self.dict.values())


