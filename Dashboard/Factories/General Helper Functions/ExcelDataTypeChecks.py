def isExcelDateType(cell):
    if cell.ctype == 3:
        return True
    else:
        return False

def isExcelNumberType(cell):
    if cell.ctype == 2:
        return True
    else:
        return False
