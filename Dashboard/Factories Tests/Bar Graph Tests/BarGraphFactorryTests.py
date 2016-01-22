import sys
sys.path.append('C:\\Python27\\Projects\\PublicDashboard\\Dashboard\\Factories\\Bar Graph')
import xlrd
import unittest
from datetime import datetime
from BarGraphFactory import Create
from BarGraphClass import BarGraph
from AxisInformationClass import AxisInformation
from PublicVariables import FORMATFLAG

class BarGraphFactoryTests(unittest.TestCase):
    def setUp(self):
        date1 = datetime(2015, 11, 15, 0, 0, 0)
        date2 = datetime(2015, 11, 22, 0, 0, 0)
        date3 = datetime(2015, 11, 29, 0, 0, 0)
        date4 = datetime(2015, 12, 6, 0, 0, 0)
        date5 = datetime(2015, 12, 13, 0, 0, 0)
        date6 = datetime(2015, 12, 20, 0, 0, 0)

        xValues = [date1, date2, date3, date4, date5, date6]
        yValues = [['45', '78', '97'], ['56', '67', '85'], ['50', '77', '90'], ['48', '57', '96'], ['70', '38', '86'], ['56', '97', '9']]

        xAxis = AxisInformation(title = u'Date', values = xValues, pointsPerEntry = 1, startRow = 7, startCol = 0, formatFlag = FORMATFLAG.none)
        yAxis = AxisInformation(title = u'Number of People', values = yValues, pointsPerEntry = 3, startRow = 7, startCol = 1, formatFlag = FORMATFLAG.none)

        self.title = u'Attendence'
        self.xAxis = xAxis
        self.yAxis = yAxis

    def test_Create(self):
        path = "C:\\Python27\\Projects\\PublicDashboard\\Dashboard\\Factories Tests\\Bar Graph Tests\\Bar_Graph_Example.xlsx"
        book = xlrd.open_workbook(path)
        first_sheet = book.sheet_by_index(0)
        actual = Create(book, first_sheet)
        self.assertEqual(actual.title, self.title)

        self.assertEqual(actual.xAxis.title, self.xAxis.title)
        self.assertEqual(actual.xAxis.values, self.xAxis.values)
        self.assertEqual(actual.xAxis.pointsPerEntry, self.xAxis.pointsPerEntry)
        self.assertEqual(actual.xAxis.startRow, self.xAxis.startRow)
        self.assertEqual(actual.xAxis.startCol, self.xAxis.startCol)
        self.assertEqual(actual.xAxis.formatFlag, self.xAxis.formatFlag)

        self.assertEqual(actual.yAxis.title, self.yAxis.title)
        self.assertEqual(actual.yAxis.values, self.yAxis.values)
        self.assertEqual(actual.yAxis.pointsPerEntry, self.yAxis.pointsPerEntry)
        self.assertEqual(actual.yAxis.startRow, self.yAxis.startRow)
        self.assertEqual(actual.yAxis.startCol, self.yAxis.startCol)
        self.assertEqual(actual.yAxis.formatFlag, self.yAxis.formatFlag)

if __name__ == '__main__':
    unittest.main()
