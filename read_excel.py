from openpyxl import load_workbook

wb = load_workbook(filename='c:Users/ywl/Desktop/demo.xlsx')
sheet_ranges = wb['Sheet']
print(sheet_ranges['A1'].value)
