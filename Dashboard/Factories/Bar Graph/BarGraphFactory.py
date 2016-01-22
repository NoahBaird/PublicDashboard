import sys
sys.path.append('C:\\Python27\\Projects\\PublicDashboard\\Dashboard\\Factories\\General Helper Functions')
from BarGraphClass import BarGraph
from AxisInformationClass import AxisInformation
from KeyFieldValueSearch import FindKeyValue
from GetDataRange import GetDataRange

def Create(book, sheet):
    '''# Checks to see if widget should be created
    if sheet.cell(1,1).value.lower() == 'false':
        print ("%s widget disabled") % (sheet.name)
        if not sheet.cell(1,1).value.lower() == 'true':
            print ("error in determining enabled state of %s") % (sheet.name)
        return None'''
    barGraphObject = BarGraph()
    xAxis = AxisInformation()
    yAxis = AxisInformation()

    barGraphObject.title = FindKeyValue(sheet, 'Graph Title').formatInfo.updatedValue
    xAxis.title = FindKeyValue(sheet, 'Horizontal Axis Title').formatInfo.updatedValue
    yAxis.title = FindKeyValue(sheet, 'Vertical Axis Title').formatInfo.updatedValue

    xValuesIndicatorCell = FindKeyValue(sheet, 'x-values')
    xAxis.startRow = xValuesIndicatorCell.row
    xAxis.startCol = xValuesIndicatorCell.column
    xAxis.formatFlag = xValuesIndicatorCell.formatInfo.formatFlag

    yValuesIndicatorCell = FindKeyValue(sheet, 'y-values')
    yAxis.startRow = yValuesIndicatorCell.row
    yAxis.startCol = yValuesIndicatorCell.column
    yAxis.formatFlag = yValuesIndicatorCell.formatInfo.formatFlag

    xAxis.pointsPerEntry = yAxis.startCol-xAxis.startCol
    yAxis.pointsPerEntry = sheet.ncols-yAxis.startCol

    xAxis.values = GetDataRange(book, sheet, xAxis.pointsPerEntry, xAxis.startRow + 1, xAxis.startCol)
    yAxis.values = GetDataRange(book, sheet, yAxis.pointsPerEntry, yAxis.startRow + 1, yAxis.startCol)

    barGraphObject.xAxis = xAxis
    barGraphObject.yAxis = yAxis
    return barGraphObject
#----------------------------------------------------------------------
import xlrd
path = "C:\\Users\\NB029380\\Documents\\TempMine\\Bar_Graph_Example.xlsx"
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
Create(book, first_sheet)
