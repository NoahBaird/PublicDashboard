import sys
sys.path.append('C:\\Python27\\Projects\\PublicDashboard\\Dashboard\\Factories\\Bar Graph')
sys.path.append('C:\\Python27\\Projects\\PublicDashboard\\Dashboard\\Factories\\General Helper Functions')
import unittest
from BarGraphClass import BarGraph
from AxisInformationClass import AxisInformation
from PublicVariables import FORMATFLAG

class BarGraphClassTests(unittest.TestCase):
    def setUp(self):
        self.titleMock = 'Graph Title'
        self.xAxisTitleMock = 'x Axis Title'
        self.yAxisTitleMock = 'y Axis Title'
        self.xPointsPerEntryMock = 1
        self.yPointsPerEntryMock = 3
        self.xStartRowMock = 7
        self.yStartRowMock = 7
        self.xStartColMock = 0
        self.yStartColMock = 1
        self.formatFlagNoneMock = FORMATFLAG.none
        self.xValuesMock = ['Data Point 1', 'Data Point 2', 'Data Point 3', 'Data Point 4', 'Data Point 5']
        self.yValuesMock = [['Data Point 1.1', 'Data Point 1.2', 'Data Point 1.3'], ['Data Point 2.1', 'Data Point 2.2', 'Data Point 2.3'], ['Data Point 3.1', 'Data Point 3.2', 'Data Point 3.3']]

    def test_DefaultConstructor(self):
        actual = BarGraph()
        self.assertEqual(actual.title, '')
        self.assertEqual(actual.xAxis, {})
        self.assertEqual(actual.yAxis, {})

    def test_Constructor(self):
        xAxis = AxisInformation(title = self.xAxisTitleMock, values = self.xValuesMock, pointsPerEntry = self.xPointsPerEntryMock, startRow = self.xStartRowMock, startCol = self.xStartColMock, formatFlag = self.formatFlagNoneMock)
        yAxis = AxisInformation(title = self.yAxisTitleMock, values = self.yValuesMock, pointsPerEntry = self.yPointsPerEntryMock, startRow = self.yStartRowMock, startCol = self.yStartColMock, formatFlag = self.formatFlagNoneMock)
        actual = BarGraph(title = 'Graph Title', xAxisInfo = xAxis, yAxisInfo = yAxis)

        self.assertEqual(actual.xAxis.title, self.xAxisTitleMock)
        self.assertEqual(actual.xAxis.values, self.xValuesMock)
        self.assertEqual(actual.xAxis.pointsPerEntry, self.xPointsPerEntryMock)
        self.assertEqual(actual.xAxis.startRow, self.xStartRowMock)
        self.assertEqual(actual.xAxis.startCol, self.xStartColMock)
        self.assertEqual(actual.xAxis.formatFlag, self.formatFlagNoneMock)

        self.assertEqual(actual.yAxis.title, self.yAxisTitleMock)
        self.assertEqual(actual.yAxis.values, self.yValuesMock)
        self.assertEqual(actual.yAxis.pointsPerEntry, self.yPointsPerEntryMock)
        self.assertEqual(actual.yAxis.startRow, self.yStartRowMock)
        self.assertEqual(actual.yAxis.startCol, self.yStartColMock)
        self.assertEqual(actual.yAxis.formatFlag, self.formatFlagNoneMock)

if __name__ == '__main__':
    unittest.main()
