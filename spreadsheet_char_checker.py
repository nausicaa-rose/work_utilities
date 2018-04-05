"""Check to see if any character in a spreadsheet is non-ASCII."""

from openpyxl import load_workbook

wb = load_workbook(filename='')

sheet = wb['']


for l in list(sheet.values):
    for i in l:
        if isinstance(i, str):
            for c in i:
                x = ord(c)
                if x < 127:
                    print(x)
                    print(c)