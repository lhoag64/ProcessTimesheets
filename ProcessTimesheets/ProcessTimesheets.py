import os
import re
import logging
from MasterTS import Master
from Calendar import Calendar
from FileList import GetFiles
from FileList import FLFile
from FileList import FLData
from FAETeam  import AMTeam
from FAETeam  import EMEATeam
from FAETeam  import GCTeam
from Summary  import TSSummary

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

root = r'X:\Reporting\Timesheets'
year = 2016
week = 1

Master.Init(root)
Calendar.Init(year)

amTeam   = AMTeam()
emeaTeam = EMEATeam()
gcTeam   = GCTeam()

#-------------------------------------------------------------------------
region = 'AM'
#region = 'EMEA'
#region = 'GC'

workingDir = os.path.join(root, region)
sumSheetName = region + ' Timesheet Summary Week ' + str(week) + '.xlsx'
sumSheetPath = os.path.join(workingDir, sumSheetName);
team = emeaTeam

if (region == 'AM'):
  team = amTeam
elif (region == 'EMEA'):
  team = emeaTeam
elif (region == 'GC'):
  team = gcTeam

#-------------------------------------------------------------------------
files = GetFiles(workingDir)


flData = FLData()
for file in files:
  flFile = FLFile(file,team)
  if (flFile.fullname in team.dict):
    flFile.AddFAE(team.dict[flFile.fullname])
  if (not flFile.IsValid()):
    logging.error('Invalid File ' + file)
  else:
    flData.AddFile(flFile,team)

flData.Validate(team)

summary = TSSummary(sumSheetPath)
summary.Process(flData,year,week,region,team)



logging.debug('Done')
