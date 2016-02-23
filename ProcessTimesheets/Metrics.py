import logging
from FAE       import FAETeam
from FAE       import FAEMember
from TimeSheet import Timesheet
from TimeSheet import TSEntry

#-----------------------------------------------------------------------
# Class Metrics
#-----------------------------------------------------------------------
class Metrics:
  #---------------------------------------------------------------------
  # Related to code, KAM, Other, Xxxxx
  #---------------------------------------------------------------------
  class Codes:
    def __init__(self):
      self.kam = Metrics.Codes.KAM()
      self.rka = Metrics.Codes.RKAM()
      self.car = Metrics.Codes.Carriers()
      self.smc = Metrics.Codes.SmallCell()
      self.mod = Metrics.Codes.MI()
      self.sem = Metrics.Codes.Semi()
      self.oth = Metrics.Codes.Other()
      self.ovr = Metrics.Codes.Overhead()
    def Update(self,entry):
      code  = entry.code.GetVal()
      hours = entry.hours.GetVal()
      if (hours != None):
        if (code != None):
          if (len(code) == 3):
            self.kam.Update(code,hours)
            self.rka.Update(code,hours)
            self.car.Update(code,hours)
            self.smc.Update(code,hours)
            self.mod.Update(code,hours)
            self.sem.Update(code,hours)
            self.oth.Update(code,hours)
            self.oth.Update(code,hours)
          elif (len(code) == 5):
            self.ovr.Update(code,hours)
    #-------------------------------------------------------------------
    class KAM:
      def __init__(self):
        self.erc = 0.0
        self.nok = 0.0
        self.alu = 0.0
        self.oth = 0.0
      def Update(self,code,hours):
            if   (code == 'ERC'): self.erc += hours
            elif (code == 'NOK'): self.nok += hours
            elif (code == 'NSN'): self.nok += hours
            elif (code == 'ALU'): self.alu += hours
            elif (code != 'OTH' and code != 'COB' and code != 'TTT'):
              self.oth += hours
    #-------------------------------------------------------------------
    class RKAM:
      def __init__(self):
        self.qcm = 0.0
        self.att = 0.0
        self.spr = 0.0
      def Update(self,code,hours):
            if   (code == 'QUA'): self.qcm += hours
            elif (code == 'ATT'): self.att += hours
            elif (code == 'SPR'): self.spr += hours
    #-------------------------------------------------------------------
    class Carriers:
      def __init__(self):
        self.att = 0.0
        self.spr = 0.0
        self.tmo = 0.0
      def Update(self,code,hours):
            if   (code == 'ATT'): self.att += hours
            elif (code == 'SPR'): self.spr += hours
            elif (code == 'TMO'): self.tmo += hours
    #-------------------------------------------------------------------
    class SmallCell:
      def __init__(self):
        self.qcm = 0.0
        self.itl = 0.0
        self.prw = 0.0
        self.spd = 0.0
      def Update(self,code,hours):
            if   (code == 'QUA'): self.qcm += hours
            elif (code == 'INT'): self.itl += hours
            elif (code == 'PRW'): self.prw += hours
            elif (code == 'SPD'): self.spd += hours
    #-------------------------------------------------------------------
    class MI:
      def __init__(self):
        self.qor = 0.0
        self.ter = 0.0
      def Update(self,code,hours):
            if   (code == 'QOR'): self.qor += hours
            elif (code == 'TER'): self.ter += hours
    #-------------------------------------------------------------------
    class Semi:
      def __init__(self):
        self.air = 0.0
        self.van = 0.0
      def Update(self,code,hours):
            if   (code == 'AIR'): self.air += hours
            elif (code == 'VAN'): self.van += hours
    #-------------------------------------------------------------------
    class Other:
      def __init__(self):
        self.oth = 0.0
        self.cob = 0.0
        self.ttt = 0.0
      def Update(self,code,hours):
        if   (code == 'OTH'): self.oth += hours
        elif (code == 'COB'): self.cob += hours
        elif (code == 'TTT'): self.ttt += hours
    #-------------------------------------------------------------------
    class Overhead:
      def __init__(self):
        self.x4x = 0.0
        self.x1x = 0.0
      def Update(self,code,hours):
        if   (code.startswith('X4')): self.x4x += hours
        elif (code.startswith('X1')): self.x1x += hours
  #---------------------------------------------------------------------
  class Team:
    def __init__(self):
      self.dmr = 0.0
      self.mi  = 0.0
    def Update(self,fae,entry):
      hours = entry.hours.GetVal()
      if (hours != None):
        if (fae.team.GetVal() == 'DMR'):
          self.dmr += hours
        elif (fae.team.GetVal() == 'MI'):
          self.mi  += hours
  #---------------------------------------------------------------------
  class Total:
    def __init__(self):
      self.tot = 0.0
      self.prm = 0.0
      self.con = 0.0
      self.lbr = 0.0
      self.trv = 0.0
      self.sby = 0.0
    def Update(self,fae,entry):
      hours = entry.hours.GetVal()
      if (hours != None):
        self.tot += hours
        wType = entry.workType.GetVal()
        if (wType != None):
          if   (wType.startswith('L')): self.lbr += hours
          elif (wType.startswith('T')): self.trv += hours
          elif (wType.startswith('S')): self.sby += hours
        fType = fae.laborType.GetVal()
        if   (fType == 'C'): self.con += hours
        elif (fType == 'P'): self.prm += hours
  #---------------------------------------------------------------------
  class FAE:
    class Fae:
      def __init__(self):
        self.hours = 0.0

    def __init__(self):
      self.dict = {}
      self.headcount = 0

    def Update(self,fae,entry):
      hours = entry.hours.GetVal()
      name  = fae.fullname.GetVal()
      if (hours != None):
        if (name not in self.dict):
          self.dict[name] = Metrics.FAE.Fae()
          # sDate = FAETeam.dict[name].startDate.asDate()
          # eDate = FAETeam.dict[name].endDate.asDate()
          # wsDate = entry.date
          # TODO: check entry date to see if it is in the week braketed by sDate and eDate
          # Don't do this here, calculate headcount someplace else
          # self.headcount += 1
      metrics = self.dict[name]
      metrics.hours += hours
      #logging.debug(fae.fullname.GetVal())
      #logging.debug(fae.team.GetVal())
      #logging.debug(fae.laborType.GetVal())
      #logging.debug(fae.loc.GetVal())
      #logging.debug(entry.code.GetVal())
      #logging.debug(entry.location.GetVal())
      #logging.debug(entry.activity.GetVal())
      #logging.debug(entry.product.GetVal())
      #logging.debug(entry.hours.GetVal())
      #logging.debug(entry.workType.GetVal())
      #logging.debug('Done')
#-----------------------------------------------------------------------
  def __init__(self,date):
    self.codes = Metrics.Codes()
    self.team  = Metrics.Team()
    self.total = Metrics.Total()
    self.fae   = Metrics.FAE()
    self.ws    = date

  def Update(self,fae,entry):
    self.codes.Update(entry)
    self.team.Update(fae,entry)
    self.total.Update(fae,entry)
    self.fae.Update(fae,entry)

  def Log(self):
    logging.debug('METRICS ' + str(self.ws) + '--------------------------------')
    logging.debug('Code Based')
    logging.debug('  Key Accounts')
    logging.debug('    ERC  : ' + str(self.codes.kam.erc))
    logging.debug('    NOK  : ' + str(self.codes.kam.nok))
    logging.debug('    ALU  : ' + str(self.codes.kam.alu))
    logging.debug('    Other: ' + str(self.codes.kam.oth))
    logging.debug('  Other')
    logging.debug('    OTH  : ' + str(self.codes.oth.oth))
    logging.debug('    COB  : ' + str(self.codes.oth.cob))
    logging.debug('    TTT  : ' + str(self.codes.oth.ttt))
    logging.debug('  Overhead')
    logging.debug('    X4x  : ' + str(self.codes.ovr.x4x))
    logging.debug('    X1x  : ' + str(self.codes.ovr.x1x))
    logging.debug('Team Based')
    logging.debug('  DMR     : ' + str(self.team.dmr))
    logging.debug('  MI      : ' + str(self.team.mi))
    logging.debug('Total Hours')
    logging.debug('  All     : ' + str(self.total.tot))
    logging.debug('  Perm    : ' + str(self.total.prm))
    logging.debug('  Cont    : ' + str(self.total.con))
    logging.debug('  Labour  : ' + str(self.total.lbr))
    logging.debug('  Travel  : ' + str(self.total.trv))
    logging.debug('  Standby : ' + str(self.total.sby))
    logging.debug('FAEs')
    logging.debug('  Headcount: ' + str(self.fae.headcount))
    for name in self.fae.dict:
      logging.debug('  ' + name.ljust(20) + ': ' + str(self.fae.dict[name].hours))
    logging.debug('Done')

