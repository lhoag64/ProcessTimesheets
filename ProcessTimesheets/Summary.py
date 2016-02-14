#import os
#import datetime
import logging
from   Calendar  import Calendar
from   TimeSheet import Timesheet
import openpyxl
from   openpyxl.workbook import Workbook
from   openpyxl.styles   import Font,Side,Border,Alignment,Color,Style
from   Metrics import Metrics


#-----------------------------------------------------------------------
# Class TSSummary
#-----------------------------------------------------------------------
class TSSummary:
  def __init__(self,fname):
    self.filename = fname
    self.sslist = []
    self.tsdict = {}
    self.week = None
    self.year = None
    self.swb  = None
    
  #---------------------------------------------------------------------
  def Process(self,tsdata,team,year,week):
    self.year = year
    self.week = week

    self.Sort(tsdata,week)

    for i,week in enumerate(self.sslist):
      wsDate = Calendar.week[i+1]
      self.tsdict[wsDate] = []
      for j,ssdata in enumerate(week):
        #logging.debug(ssdata.
        ts = Timesheet(ssdata, wsDate)
        ts.ReadFile()
        self.tsdict[wsDate].append(ts)
 
    self.createWorkbook()
    self.writeRawDataSheet()
    self.saveWorkbook()

  #---------------------------------------------------------------------
  def createWorkbook(self):
    self.swb = Workbook()
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

    wsRow = 2
    wsCol = 2

    #-------------------------------------------------------------------
    # Process each week
    #-------------------------------------------------------------------
    for weekIndex in range(1,self.week+1): 
      wsDate = Calendar.week[weekIndex]
      tslist = self.tsdict[wsDate]
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

          # end of entry
          wsRow += 1

      #---------------------------------------------------------------
      # end of a week
      wsRow += 2





    logging.debug('Done') 


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






