from PublicVariables import FORMATFLAGINDICATOR
from PublicVariables import FORMATFLAG
from FormatClass import FormatClass
from re import sub

def SetFormatFlag(label):
    formatField = FORMATFLAG.none
    updatedValueField = label
    if FORMATFLAGINDICATOR['CURRENCY'] in label:
        formatField = FORMATFLAG.currency
        updatedValueField = label.replace(FORMATFLAGINDICATOR['CURRENCY'], '').rstrip()
    return FormatClass(formatField, updatedValueField)