import sys
sys.path.append('C:\\Python27\\Projects\\PublicDashboard\\Dashboard\\Factories\\General Helper Functions')
import unittest
from SetFormatFlag import SetFormatFlag
from FormatClass import FormatClass
from PublicVariables import FORMATFLAG

class SetFORMATFLAGsTests(unittest.TestCase):
    def setUp(self):
        self.noFormatLabel = u'aBc'
        self.currencyUnformatLabel = u'Dollars (__currency__)'
        self.currencyFormatedLabel = u'Dollars'

        self.noFormatClass = FormatClass(self.noFormatLabel, FORMATFLAG.none)
        self.currencyFormatClass = FormatClass(self.currencyUnformatLabel, FORMATFLAG.currency)

    def test_SetFomratFlagNoFormat(self):
        actual = SetFormatFlag(self.noFormatLabel)
        self.assertIsInstance(actual, FormatClass)
        self.assertEqual(actual.formatFlag, FORMATFLAG.none)
        self.assertEqual(actual.updatedValue, self.noFormatLabel)

    def test_SetFomratFlagCurrency(self):
        actual = SetFormatFlag(self.currencyUnformatLabel)
        self.assertIsInstance(actual, FormatClass)
        self.assertEqual(actual.formatFlag, FORMATFLAG.currency)
        self.assertEqual(actual.updatedValue, self.currencyFormatedLabel)

if __name__ == '__main__':
    unittest.main()
