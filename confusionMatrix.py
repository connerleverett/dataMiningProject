import xlsxwriter
import os
import sys

#This makes the excel sheet----------------------------------------------------------------------
#Numbering System can be found here: http://www.infoplease.com/ipa/A0763770.html			
dictOfNumberedStates = {'Delaware':1,'Pennsylvania':2,'NewJersey':3,'Georgia':4,
'Connecticut':5,'Massachusetts':6,'Maryland':7,'SouthCarolina':8,'NewHampshire':9,
'Virginia':10,'NewYork':11,'NorthCarolina':12,'RhodeIsland':13,'Vermont':14,'Kentucky':15,
'Tennessee':16,'Ohio':17,'Louisiana':18,'Indiana':19,'Mississippi':20,'Illinois':21,
'Alabama':22,'Maine':23,'Missouri':24,'Arkansas':25,'Michigan':26,'Florida':27,
'Texas':28,'Iowa':29,'Wisconsin':30,'California':31,'Minnesota':32,'Oregon':33,
'Kansas':34,'WestVirginia':35,'Nevada':36,'Nebraska':37,'Colorado':38,'NorthDakota':39,
'SouthDakota':40,'Montana':41,'Washington':42,'Idaho':43,'Wyoming':44,'Utah':45,'Oklahoma':46,
'NewMexico':47,'Arizona':48,'DC':49}

#Excel Sheet which is being written to
workbook = xlsxwriter.Workbook('confusionMatrix.xlsx')

#Adding a worksheet to the workbook
worksheet=workbook.add_worksheet()

#Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

for x in range(len(dictOfNumberedStates)):
	#Extract the key which contains that value
	state = dictOfNumberedStates.keys()[dictOfNumberedStates.values().index(x+1)]
	worksheet.write(x+1,0, state,bold)
	worksheet.write(0,x+1,state,bold)

#-------------------------------------------------------------------------------------------------

#Initalize the confusion matrix to keep track
confusionMatrix =  [[0 for x in range(49)] for x in range(49)]

#This is keeping track of what value should be added
#confusionMatrix[ACTUAL CLASSIFICATION][PREDICTED CLASSIFICATION] += 1

#Then this is needed at the end to convert the confusionMatrix to an excel file
for x in range(len(confusionMatrix)):
	for y in range(len(confusionMatrix[0])):
		worksheet.write(x+1,y+1, confusionMatrix[x][y])

#This is needed to save the excel file
workbook.close()

