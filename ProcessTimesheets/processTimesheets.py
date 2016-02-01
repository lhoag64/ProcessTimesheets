#import os
import logging
import processTree
#import parseTimesheet



root = r'X:\Timesheets.Sandox'

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

files = processTree.getFiles(root)

logging.debug('Done')



#for dirName, subDirs, fNames in os.walk(root):
#  logging.debug('dirName ' + dirName)
#  for subDir in subDirs:
#    logging.debug(' subDir ' + subDir)
#    for fName in fNames:
#      logging.debug('  fname ' + fName)
# 
#os.walk 
#

#print(__name__)
#parseTimesheet.parseTS()