from ExcelDateToObject import convertDateTime
from ExcelDataTypeChecks import isExcelDateType
from ExcelDataTypeChecks import isExcelNumberType

def GetDataRange(book, sheet, pointsPerEntry, startRow, startCol):
    values = []
    for row in range(startRow, sheet.nrows):
        if (pointsPerEntry != 1):
            rowValues = []
            for column in range(startCol, startCol + pointsPerEntry):
                cell = sheet.cell(row, column)
                rowValues.append(FormatCellValue(cell, book))
            values.append(rowValues)
        else:
            cell = sheet.cell(row, startCol)
            values.append(FormatCellValue(cell, book))
    return values

def FormatCellValue(cell, book):
    if isExcelDateType(cell):
        return convertDateTime(cell.value, book)
    elif (isExcelNumberType(cell)):
        return '{0:n}'.format(cell.value)
    else:
        return cell.value
