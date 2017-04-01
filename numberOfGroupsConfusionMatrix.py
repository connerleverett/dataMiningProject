import xlrd
import os
import sys
from jenks import jenks

#Excel sheet which is being read
book = xlrd.open_workbook(r'C:\Conner\SENG474\dataMiningProject\confusionMatrix.xlsx')
first_sheet=book.sheet_by_index(0)

matrixList = []

for row in range(1,50):
	for col in range(1,50):
		if (row!=col):
			if (first_sheet.cell(row,col).value!=0):
				matrixList.append(first_sheet.cell(row,col).value)
		
		
print jenks(matrixList,3)	