def FindKeyValue(sheet, searchKey):
    searchKey = lower(sub('[\s+]', '', searchKey))
    for row in sheet.nrows:
        for column in sheet.ncols:
            condensedValue = lower(sub('[\s+]', '', sheet.cell(row, column).value))
            if searchKey == condensedValue:
                return (sheet.cell(row, column + 1).value, row, column)