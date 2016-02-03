import os
import os.path
import logging

finished = []

def getFiles(root):
  list = []
  #logging.debug(root)
  walk(root, list)
  return list

def walk(rootdir, list):
  for curdir, subdirs, files in os.walk(rootdir):
    #logging.debug(curdir)
    for file in files:
      if (file.startswith('Timesheet')):
        fname = os.path.join(rootdir,file)
        #logging.debug(fname)
        list.append(fname)
    if (subdirs):
      for subdir in subdirs:
        dir = os.path.join(rootdir,subdir)
        walk(dir, list)
    break

