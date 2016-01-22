from xlrd import sheet

class ExtendedCell(sheet.Cell):
    def __init__(self, cellObj, row, column, formatInfo):
        self.ctype = cellObj.ctype
        self.value = cellObj.value
        self.xf_index = cellObj.xf_index
        self.row = row
        self.column = column
        self.formatInfo = formatInfo
