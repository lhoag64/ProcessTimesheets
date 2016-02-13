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


root = r'X:\Timesheets.Sandox'
year = 2016
week = 3

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

Master.Init(root)
Calendar.Init(year)

files = GetFiles(root)

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

summary.Process(flData, team, year, week)



logging.debug('Done')
