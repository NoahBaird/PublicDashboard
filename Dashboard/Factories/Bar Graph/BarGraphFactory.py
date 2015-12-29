import xlrd
from BarGraphClass import BarGraph
from KeyFieldValueSearch import FindKeyValue
from GetDataRange import GetDataRange

def Create(book, sheet):
    '''# Checks to see if widget should be created
    if sheet.cell(1,1).value.lower() == 'false':
        print ("%s widget disabled") % (sheet.name)
        if not sheet.cell(1,1).value.lower() == 'true':
            print ("error in determining enabled state of %s") % (sheet.name)
        return None'''
    
    graphTitle = FindKeyValue(sheet, 'Graph TItle')[0]
    xAxisTitle = FindKeyValue(sheet, 'Vertical Axis Title')[0]
    yAxisTitle = FindKeyValue(sheet, 'Horizontal Axis Title')[0]
    xValuesKeyField = FindKeyValue(sheet, 'x-values')
    xValuesStartRow = xValuesKeyField[1]
    xValuesStartCol = xValuesKeyField[2]
    yValuesKeyField = FindKeyValue(sheet, 'y-values')
    yValuesStartRow = yValuesKeyField[1]
    yValuesStartCol = yValuesKeyField[2]

    xValues = GetDataRange(xValuesStartRow, xValuesStartCol, yValuesStartRow, yValuesStartCol)
    yValues = GetDataRange(yValuesStartRow, yValuesStartCol, sheet.nrows, sheet.ncols)

    barGraphObject = BarGraph(graphTitle, xAxisTitle, yAxisTitle, yValuesStartCol-xValuesStartCol, sheet.ncols-yValuesStartCol, xValues, yValues)
    return barGraphObject
#----------------------------------------------------------------------
path = "C:\\Users\\NB029380\\Documents\\TempMine\\Bar_Graph_Example.xlsx"
book = xlrd.open_workbook(path)
first_sheet = book.sheet_by_index(0)
Create(book, first_sheet)
