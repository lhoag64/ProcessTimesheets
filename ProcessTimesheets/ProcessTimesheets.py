import os
import re
import logging
from MasterTS import Master
from Calendar import Calendar
from FileList import GetFiles
from FileList import FLFile
from FileList import FLData
from FAE      import FAETeam
from Summary  import TSSummary


root = r'X:\Reporting\Timesheets.Sandox'
year = 2016
week = 7
sumSheetName = r'AM Timesheet Summary Week 7.xlsx'
sumSheetPath = os.path.join(root, sumSheetName);

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

Master.Init(root)
Calendar.Init(year)
FAETeam.Init()

files = GetFiles(root)

#team   = FAETeam()
flData = FLData()
for file in files:
  flFile = FLFile(file)
  if (flFile.fullname in FAETeam.dict):
    flFile.AddFAE(FAETeam.dict[flFile.fullname])
  if (not flFile.IsValid()):
    logging.error('Invalid File ' + file)
  else:
    flFile.Log()
    flData.AddFile(flFile)

flData.Log()
flData.Validate()

summary = TSSummary(sumSheetPath)
summary.Process(flData,year,week)



logging.debug('Done')
