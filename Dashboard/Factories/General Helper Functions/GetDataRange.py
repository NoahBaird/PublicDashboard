from ExcelDateToObject import convertDateTime

def GetDataRange(startRow, startCol, endRow, endCol):
    values = []
    for row in range(startRow, endRow):
        rowValues = []
        for column in range(startCol, endCol):
            cell = sheet.cell(row, column)
            if cell.ctype == 3:
                rowValues.append(convertDateTime(cell.value))
            else:
                rowValues.append(cell.value)
        values.append(rowValues)
    return values