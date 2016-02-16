#import os
#import datetime
import logging
from   Calendar  import Calendar
from   TimeSheet import Timesheet
import openpyxl
from   openpyxl.workbook import Workbook
from   openpyxl.styles   import Font,Side,Border,Alignment,Color,Style
from   openpyxl.styles.colors import RED
from   FAE     import FAETeam
from   Metrics import Metrics


#-----------------------------------------------------------------------
# Class TSSummary
#-----------------------------------------------------------------------
class TSSummary:
  def __init__(self,fname):
    self.filename = fname
    self.sslist  = []         # list of spreadsheets by week
    self.tsdict  = {}         # dict of timesheet data by week
    self.week    = None       # current week number
    self.year    = None       # year of query
    self.swb     = None       # summary workbook
    self.metrics = {}         # summary metrics
     
  #---------------------------------------------------------------------
  def Process(self,tsdata,year,week):
    self.year = year
    self.week = week

    self.Sort(tsdata,week)

    for i,week in enumerate(self.sslist):
      wsDate = Calendar.week[i+1]
      self.tsdict[wsDate] = []
      for j,ssdata in enumerate(week):
        ts = Timesheet(ssdata, wsDate)
        ts.ReadFile()
        self.tsdict[wsDate].append(ts)
 
    self.createWorkbook()
    self.writeRawDataSheet()
    self.saveWorkbook()

  #---------------------------------------------------------------------
  def createWorkbook(self):
    self.swb = Workbook()
    self.swb.create_sheet('AM Charts')
    self.swb.create_sheet('AM Tables')
    self.swb.create_sheet('AM Metrics')
    self.swb.create_sheet('AM Data')

  #---------------------------------------------------------------------
  def saveWorkbook(self):
    self.swb.save(self.filename)

  #---------------------------------------------------------------------
  def setCell(self,cell,align,fmt,value):
    if (align == 'C'):
      align = Alignment(horizontal='center',vertical='center')
    elif (align == 'L'):
      align = Alignment(horizontal='left',vertical='center')
    else:
      align = Alignment(horizontal='right',vertical='center')

    fmt = None
    if (fmt == 'F'):
      fmt = '0.00'

    side   = Side(style='thin')
    border = Border(left=side,right=side,top=side,bottom=side)
    style  = Style(border=border,alignment=align,number_format=fmt)

    cell.style = style
    cell.value = value

  #---------------------------------------------------------------------
  def flagCell(self,cell):
    side   = Side(style='medium',color=RED)
    border = Border(left=side,right=side,top=side,bottom=side)
    style  = Style(border=border)
    cell.style = style

  #---------------------------------------------------------------------
  def writeRawDataSheet(self):
    ws = self.swb.get_sheet_by_name('AM Data')

    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width =  3
    ws.column_dimensions['D'].width =  5
    ws.column_dimensions['E'].width =  3
    ws.column_dimensions['F'].width = 11
    ws.column_dimensions['G'].width = 11
    ws.column_dimensions['H'].width =  7
    ws.column_dimensions['I'].width =  5
    ws.column_dimensions['J'].width =  5
    ws.column_dimensions['K'].width =  5
    ws.column_dimensions['L'].width =  5
    ws.column_dimensions['M'].width = 10
    ws.column_dimensions['N'].width = 80

    wsRow = 2
    wsCol = 2

    #-------------------------------------------------------------------
    # Process each week
    #-------------------------------------------------------------------
    for weekIndex in range(1,self.week+1): 
      wsDate = Calendar.week[weekIndex]
      tslist = self.tsdict[wsDate]
      metrics = Metrics(wsDate)
      #-----------------------------------------------------------------
      # Process timesheet specific informaton
      #-----------------------------------------------------------------
      for ts in tslist:
        fae = ts.ssdata.fae

        #---------------------------------------------------------------
        # Process each entry in the timesheet
        #---------------------------------------------------------------
        for entry in ts.entries:
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 0),'L','G',fae.fullname.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 1),'C','G',fae.laborType.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 2),'C','G',fae.team.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 3),'C','G',fae.loc.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 4),'C','G',ts.ssdata.wsDate.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 5),'C','D',entry.date.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 6),'C','G',entry.code.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 7),'C','G',entry.location.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 8),'C','G',entry.activity.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+ 9),'C','G',entry.product.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+10),'R','F',entry.hours.GetWSVal())
          self.setCell(ws.cell(row=wsRow,column=wsCol+11),'C','G',entry.workType.GetWSVal())

          # Flag as red things to check
          if (entry.code.GetVal() == 'OTH'):
            self.flagCell(ws.cell(row=wsRow,column=wsCol+ 6))
            self.setCell(ws.cell(row=wsRow,column=wsCol+12),'L','G',entry.note.GetWSVal())
            self.flagCell(ws.cell(row=wsRow,column=wsCol+12))

          if (entry.code.GetVal() == 5):
            if (entry.location.GetVal() != None):
              self.flagCell(ws.cell(row=wsRow,column=wsCol+ 7))
            if (entry.activity.GetVal() != None):
              self.flagCell(ws.cell(row=wsRow,column=wsCol+ 8))
            if (entry.product.GetVal() != None):
              self.flagCell(ws.cell(row=wsRow,column=wsCol+ 9))

          if (entry.location.GetVal() == 128):
            self.flagCell(ws.cell(row=wsRow,column=wsCol+ 7))
            self.setCell(ws.cell(row=wsRow,column=wsCol+12),'L','G',entry.note.GetWSVal())
            self.flagCell(ws.cell(row=wsRow,column=wsCol+12))

          if (entry.product.GetVal() == 22):
            self.flagCell(ws.cell(row=wsRow,column=wsCol+ 9))
            self.setCell(ws.cell(row=wsRow,column=wsCol+12),'L','G',entry.note.GetWSVal())
            self.flagCell(ws.cell(row=wsRow,column=wsCol+12))

          if (entry.hours.GetVal() == None):
            self.flagCell(ws.cell(row=wsRow,column=wsCol+10))

          if (entry.workType.GetVal() == None):
            self.flagCell(ws.cell(row=wsRow,column=wsCol+11))

          metrics.Update(fae,entry)

          # end of entry
          wsRow += 1

      #---------------------------------------------------------------
      # end of a week
      self.metrics[wsDate] = metrics
      wsRow += 2

    #-----------------------------------------------------------------
    # Write out raw metrics
    #-----------------------------------------------------------------
    #for i in range(1,self.week+1):
    #  wsDate = Calendar.week[i]
    #  metrics = self.metrics[wsDate]
    #  metrics.Log()

    wsRow = 2
    wsCol = 2

    ws = self.swb.get_sheet_by_name('AM Metrics')

    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 10

    self.setCell(ws.cell(row= 2,column=wsCol+0),'L','G','METRICS')
    self.setCell(ws.cell(row= 3,column=wsCol+0),'L','G','  Code Based')
    self.setCell(ws.cell(row= 4,column=wsCol+0),'L','G','    Key Accounts')
    self.setCell(ws.cell(row= 5,column=wsCol+0),'L','G','      ERC')
    self.setCell(ws.cell(row= 6,column=wsCol+0),'L','G','      NOK')
    self.setCell(ws.cell(row= 7,column=wsCol+0),'L','G','      ALU')
    self.setCell(ws.cell(row= 8,column=wsCol+0),'L','G','      Other')
    self.setCell(ws.cell(row= 9,column=wsCol+0),'L','G','    Others')
    self.setCell(ws.cell(row=10,column=wsCol+0),'L','G','      OTH')
    self.setCell(ws.cell(row=11,column=wsCol+0),'L','G','      COB')
    self.setCell(ws.cell(row=12,column=wsCol+0),'L','G','      TTT')
    self.setCell(ws.cell(row=13,column=wsCol+0),'L','G','    Overhead')
    self.setCell(ws.cell(row=14,column=wsCol+0),'L','G','      X4x')
    self.setCell(ws.cell(row=15,column=wsCol+0),'L','G','      X1x')
    self.setCell(ws.cell(row=16,column=wsCol+0),'L','G','  Team Based')
    self.setCell(ws.cell(row=17,column=wsCol+0),'L','G','    DMR')
    self.setCell(ws.cell(row=18,column=wsCol+0),'L','G','    MI')
    self.setCell(ws.cell(row=19,column=wsCol+0),'L','G','  Total Hours')
    self.setCell(ws.cell(row=20,column=wsCol+0),'L','G','    All')
    self.setCell(ws.cell(row=21,column=wsCol+0),'L','G','    Permenent')
    self.setCell(ws.cell(row=22,column=wsCol+0),'L','G','    Contract')
    self.setCell(ws.cell(row=23,column=wsCol+0),'L','G','    Labour')
    self.setCell(ws.cell(row=24,column=wsCol+0),'L','G','    Travel')
    self.setCell(ws.cell(row=25,column=wsCol+0),'L','G','    Standby')
    self.setCell(ws.cell(row=26,column=wsCol+0),'L','G','  FAEs')
    rowoffs = 0
    for fae in FAETeam.list:
      name = fae.fullname.GetVal()
      self.setCell(ws.cell(row=27+rowoffs,column=wsCol+0),'L','G','    ' + name)
      rowoffs += 1


    for i in range(1,self.week+1):
      wsDate = Calendar.week[i]
      metrics = self.metrics[wsDate]
      self.setCell(ws.cell(row= 3,column=wsCol+0+i),'C','G',str(wsDate))
      self.setCell(ws.cell(row= 4,column=wsCol+0+i),'C','G',str(i))
      self.setCell(ws.cell(row= 5,column=wsCol+0+i),'L','G',metrics.codes.kam.erc)
      self.setCell(ws.cell(row= 6,column=wsCol+0+i),'L','G',metrics.codes.kam.nok)
      self.setCell(ws.cell(row= 7,column=wsCol+0+i),'L','G',metrics.codes.kam.alu)
      self.setCell(ws.cell(row= 8,column=wsCol+0+i),'L','G',metrics.codes.kam.oth)
      self.setCell(ws.cell(row=10,column=wsCol+0+i),'L','G',metrics.codes.oth.oth)
      self.setCell(ws.cell(row=11,column=wsCol+0+i),'L','G',metrics.codes.oth.cob)
      self.setCell(ws.cell(row=12,column=wsCol+0+i),'L','G',metrics.codes.oth.ttt)
      self.setCell(ws.cell(row=14,column=wsCol+0+i),'L','G',metrics.codes.ovr.x4x)
      self.setCell(ws.cell(row=15,column=wsCol+0+i),'L','G',metrics.codes.ovr.x1x)
      self.setCell(ws.cell(row=17,column=wsCol+0+i),'L','G',metrics.team.dmr)
      self.setCell(ws.cell(row=18,column=wsCol+0+i),'L','G',metrics.team.mi)
      self.setCell(ws.cell(row=20,column=wsCol+0+i),'L','G',metrics.total.tot)
      self.setCell(ws.cell(row=21,column=wsCol+0+i),'L','G',metrics.total.prm)
      self.setCell(ws.cell(row=22,column=wsCol+0+i),'L','G',metrics.total.con)
      self.setCell(ws.cell(row=23,column=wsCol+0+i),'L','G',metrics.total.lbr)
      self.setCell(ws.cell(row=24,column=wsCol+0+i),'L','G',metrics.total.trv)
      self.setCell(ws.cell(row=25,column=wsCol+0+i),'L','G',metrics.total.sby)
      rowoffs = 0
      for fae in FAETeam.list:
        name = fae.fullname.GetVal()
        if (name in metrics.fae.dict):
          hours = metrics.fae.dict[name].hours
        else:
          hours = None
        self.setCell(ws.cell(row=27+rowoffs,column=wsCol+0+i),'L','F',hours)
        if (hours == None):
          self.flagCell(ws.cell(row=27+rowoffs,column=wsCol+0+i))

        rowoffs += 1


#      for fae in FAETeam.list:
#        logging.debug(str(fae.team).ljust(3) + ' ' + str(fae.loc) + ' ' + str(fae.lname).ljust(12))
#
#      for fae in FAETeam.list:
#        name = fae.fullname.GetVal()
#        logging.debug(name + '  ' + str(metrics.fae.dict[name].hours))
#      logging.debug('Done')
#
#    logging.debug('Done') 


  #---------------------------------------------------------------------
  # Print the raw date, a good example to run through the data
  #---------------------------------------------------------------------
#  def Print(self):
#    for i in range(1,self.week+1): 
#      wsDate = Calendar.week[i]
#      tslist = self.tsdict[wsDate]
#      for j in tslist:
#        faeName = j.ssdata.fae.fullname.ljust(21)
#        faeType = j.ssdata.fae.laborType
#        faeTeam = j.ssdata.fae.team.ljust(3)
#        faeLoc  = j.ssdata.fae.loc
#        ws      = str(j.ssdata.wsDate)
#        we      = str(j.ssdata.weDate)
#        for k in j.entries:
#          wDate  = str(k.date)
#          wCode  = str(k.code).ljust(5)
#          wLoc   = str(k.location).ljust(3)
#          wAct   = str(k.activity).ljust(2)
#          wProd  = str(k.product).ljust(2)
#          wHours = str(k.hours).ljust(5)
#          wLtd   = str(k.workType).ljust(10)
#          logging.debug \
#            (faeName + '|' + faeType + '|' + faeTeam + '|' + faeLoc + '|' + \
#             ws      + '|' + we      + '|' + wDate   + '|' + \
#             wCode   + '|' + wLoc    + '|' + wAct    + '|' + wProd + '|' + \
#             wHours  + '|' + wLtd)
#    logging.debug('Done') 

  #-----------------------------------------------------------------------
  def Sort(self,tsdata,week):
    self.sslist = []
    for i in range(1,week+1):
      list = []
      dict = {}
      wsDate = Calendar.week[i]
      dict = tsdata.weeks[wsDate]
      for key,value in dict.items():
        list.append(value)
      self.sslist.append(sorted(list))
 
    #for i,week in enumerate(self.sslist):
    #  logging.debug(Calendar.week[i+1])
    #  for j,item in enumerate(week):
    #    logging.debug(item.fae.team + ' ' + item.fae.loc + ' ' + item.fae.fullname)
        
    #logging.debug('sorted list')






