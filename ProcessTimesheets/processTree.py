import os
import logging

finished = []

def getFiles(root):
  list = [];
  logging.debug(root)
  walk(root)
  return list

def walk(rootdir):
    for curdir, subdirs, files in os.walk(rootdir):
      logging.debug(curdir)
      for file in files:
        logging.debug(os.path.join(rootdir,file))
      if (subdirs):
        for subdir in subdirs:
          dir = os.path.join(rootdir,subdir)
          walk(dir)
      break

'''
def walk(rootdir):
    for curdir, subdirs, files in os.walk(rootdir):
      #logging.debug('called os.walk')
      logging.debug(curdir)
      #if (curdir not in finished):
      for file in files:
        logging.debug(os.path.join(rootdir,file))
      if (subdirs):
        for subdir in subdirs:
          #logging.debug(subdirs)
          dir = os.path.join(rootdir,subdir)
          #logging.debug(dir)
          #logging.debug('--- call walk ---')
          walk(dir)
          #logging.debug('--- exit walk ---')
      #logging.debug('break curdir = ' + curdir)
      break
'''
'''
def walk(rootdir):
  logging.debug(finished)
  if (rootdir not in finished):
    for curdir, subdirs, files in os.walk(rootdir):
      logging.debug('called os.walk')
      logging.debug('curdir = ' + curdir)
      #if (curdir not in finished):
      for file in files:
        logging.debug(os.path.join(rootdir,file))
      if (subdirs):
        for subdir in subdirs:
          #logging.debug(subdirs)
          dir = os.path.join(rootdir,subdir)
          logging.debug(dir)
          #logging.debug('--- call walk ---')
          walk(dir)
          #logging.debug('--- exit walk ---')
      finished.append(curdir)
      break
'''
