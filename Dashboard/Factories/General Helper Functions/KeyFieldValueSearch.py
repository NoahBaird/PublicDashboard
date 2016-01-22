from re import sub
from SetFormatFlag import SetFormatFlag
from ExtendedCellClass import ExtendedCell

def FindKeyValue(sheet, searchKey):
    searchKey = sub('[^A-Za-z0-9]+|[\s+]', '', searchKey).lower()
    for row in range(sheet.nrows):
        for column in range(sheet.ncols):
            condensedValue = sub('[^A-Za-z0-9]+|[\s+]', '', str(sheet.cell(row, column).value)).lower()
            if searchKey == condensedValue:
                cell = sheet.cell(row, column + 1)
                formatInfo = SetFormatFlag(cell.value)
                return ExtendedCell(cell, row, column, formatInfo)
