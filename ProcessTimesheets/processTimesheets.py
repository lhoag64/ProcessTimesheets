import os
import re
import logging
import processTree
from classes import TSFileNameInfo
#import parseTimesheet


root = r'X:\Timesheets.Sandox'

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

files = processTree.getFiles(root)

weeks = []
tsfileinfo = {}
for file in files:
  fnameinfo = TSFileNameInfo(file)
  if (not fnameinfo.IsValid()):
    logging.error('Invalid File ' + file)
  else:
    fnameinfo.Log()
  if (fnameinfo.wsDate not in tsfileinfo.keys()):
    tsfileinfo[fnameinfo.wsDate] = []
    weeks.append(fnameinfo.wsDate)
  tsfileinfo[fnameinfo.wsDate].append(fnameinfo)

weeks.sort()

for i in range(0, len(weeks)):
  logging.debug(weeks[i])
  tsfileinfo[weeks[i]].sort(key=lambda obj: obj.lname)
  for j in range(0, len(tsfileinfo[weeks[i]])):
     tsfileinfo[weeks[i]][j].Log()

#for j,k oin
#  for j in range(0, len(i)):
#    i[j].Log()
  

logging.debug('Done')
