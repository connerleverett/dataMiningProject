'''
	This program removes both unneccesary puncuation and 'https', 't', and 'co', turns all words to lowercase, 
	as well as removes common english stop words and adds weight to location specific words.
	Weight is simply added by doubling the amount the word shows in the cleaned tweet.
	Stop words taken from 'http://www.ranks.nl/stopwords'. 
'''

import re

# -------------Change input file name here-----------------
file = open('trainTest.txt', 'rt')
file2 = open('stopwords.txt', 'rt')
file3 = open('listOfStatesAndCities.txt', 'rt')
outputFile = open('cleanedTrainDataAddWeight.txt', 'w')

D = []

for x in file:
	D.append(x.strip())
	
stopWords = ['https', 't', 'co']

for x in file2:
	stopWords.append(x.strip())

locationWords = []

for x in file3:
	x = x.lower()
	locationWords.append(x.strip())

V = []
#numTermsInV is all unique words
numTermsInV = 0
for x in D:
	x = x.lower()
	wordsInTweet = re.sub("[^\w']", " ",  x).split()
	cleanedTweet = ''
	for num in range(0, len(wordsInTweet)):
		if (wordsInTweet[num] == 'co'):
			if (wordsInTweet[num - 1] != 't'):
				cleanedTweet = cleanedTweet + ' ' + wordsInTweet[num] + ' ' + wordsInTweet[num]
				num = num + 1
		elif (wordsInTweet[num] in locationWords):
			cleanedTweet = cleanedTweet + ' ' + wordsInTweet[num] + ' ' + wordsInTweet[num]
			num = num + 1
		elif (wordsInTweet[num] not in stopWords):
			cleanedTweet = cleanedTweet + ' ' + wordsInTweet[num]
	outputFile.write(cleanedTweet + '\n')

outputFile.close()