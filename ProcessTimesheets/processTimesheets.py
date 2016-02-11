import os
import re
import logging
import processTree
from classes import TSFile
#from classes import TSInfo
from classes import TSData
from classes import FAETeam
from classes import TSSummary
from classes import TSCalendar
#import parseTimesheet


root = r'X:\Timesheets.Sandox'

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

files = processTree.getFiles(root)

team   = FAETeam()
tsdata = TSData()
for file in files:
  tsfile = TSFile(file)
  if (tsfile.fullname in team.members):
    tsfile.AddFAE(team.members[tsfile.fullname])
  if (not tsfile.IsValid()):
    logging.error('Invalid File ' + file)
  else:
    tsfile.Log()
    tsdata.AddFile(tsfile)

tsdata.Log()
tsdata.Validate(team)

summary = TSSummary()

summary.Process(tsdata, team, 2016, 3)

"""
  for i in weeks:
    if (i != tsinfo.wsDate):
      #tsfileinfo[fnameinfo.wsDate] = []
      weeks.append(fnameinfo.wsDate)
      break;
  #tsfileinfo[fnameinfo.wsDate].append(fnameinfo)

weeks.sort()

for i in range(0, len(weeks)):
  logging.debug(weeks[i])
  #tsfileinfo[weeks[i]].sort(key=lambda obj: obj.lname)
  #for j in range(0, len(tsfileinfo[weeks[i]])):
  #   tsfileinfo[weeks[i]][j].Log()

#for j,k oin
#  for j in range(0, len(i)):
#    i[j].Log()
"""

logging.debug('Done')
