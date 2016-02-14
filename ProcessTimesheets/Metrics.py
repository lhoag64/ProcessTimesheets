from FAE       import FAEMember
from TimeSheet import Timesheet

#-----------------------------------------------------------------------
# Class Metrics
#-----------------------------------------------------------------------
class Metrics:
  #---------------------------------------------------------------------
  class KAM:
    def __init__(self):
      Reset()

    def Reset(self):
      erc = 0.0
      nok = 0.0
      alu = 0.0

  #---------------------------------------------------------------------
  class Total:
    def __init__(self):
      Reset()

    def Reset(self):
      all_hours  = 0.0
      perm_hours = 0.0
      cont_hours = 0.0

  #---------------------------------------------------------------------
  class FAE:
    def __init__(self):
      dict = {}
      Reset()

    def Reset(self):
      pass
            
#-----------------------------------------------------------------------
  def __init__(self):
    kam = KAM()
    tot = Total()
    fae = FAE()

  def Reset():
    kam.Reset()
    tot.Reset()
    fae.Reset()

  def Update(fae,ts,entry):
    pass