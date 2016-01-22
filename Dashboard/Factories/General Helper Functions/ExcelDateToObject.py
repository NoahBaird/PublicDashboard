def convertDateTime(xlDate, book):
    from datetime import datetime
    from xlrd import xldate_as_tuple
    dateAsTuple = xldate_as_tuple(xlDate, book.datemode)
    dateObject = datetime(dateAsTuple[0], dateAsTuple[1], dateAsTuple[2], dateAsTuple[3], dateAsTuple[4], dateAsTuple[5])
    return dateObject
