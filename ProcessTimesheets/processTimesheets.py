import os
import re
import logging
import processTree
from classes import FLFile
#from classes import TSInfo
from classes import FLData
from classes import FAETeam
from classes import TSSummary
from classes import Calendar
#import parseTimesheet


root = r'X:\Timesheets.Sandox'

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

files = processTree.getFiles(root)

team   = FAETeam()
flData = FLData()
for file in files:
  flFile = FLFile(file)
  if (flFile.fullname in team.members):
    flFile.AddFAE(team.members[flFile.fullname])
  if (not flFile.IsValid()):
    logging.error('Invalid File ' + file)
  else:
    flFile.Log()
    flData.AddFile(flFile)

flData.Log()
flData.Validate(team)

summary = TSSummary()

summary.Process(flData, team, 2016, 3)

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
