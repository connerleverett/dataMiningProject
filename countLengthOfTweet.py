'''
	This program removes both unneccesary punctuation and 'https', 't', and 'co', as well as turns all words into lower case. 
'''

import re

# -------------Change input file name here-----------------
file = open('cleanedTrainData.txt', 'rt')
outputFile = open('cleanedTrainDataLengths.txt', 'w')

D = []

for x in file:
	D.append(x.strip())
	
for x in D:
	wordsInTweet = x.split()
	outputFile.write(str(len(wordsInTweet)) + '\n')

outputFile.close()