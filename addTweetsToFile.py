import os
import sys

tweetFile = open('cleanedTrainData48.txt', 'rt')
classificationFile = open('fixedClassification48.txt','rt')

tweetList = []
classificationList = []

#Count number of lines
tweetCount = 0
for line in tweetFile:
	tweetCount +=1
	tweetList.append(line)
	
classificationCount = 0
for line in classificationFile:
	classificationCount +=1
	classificationList.append(line.strip())
	
if classificationCount!=tweetCount:
	print "Oh fuck"
	
if not os.path.exists(r'C:\Conner\SENG474\dataMiningProject\classifications'):
    os.makedirs(r'C:\Conner\SENG474\dataMiningProject\classifications')

	

for x in range(0,49):
	if not os.path.exists(r'C:\Conner\SENG474\dataMiningProject\classifications\\'+str(x)):
		os.makedirs(r'C:\Conner\SENG474\dataMiningProject\classifications\\'+str(x))	
	

save_path = r'C:\Conner\SENG474\dataMiningProject/classifications/'


for num in range(0,tweetCount):
	name_of_file = "tweet"+str(num)+'.txt'
	classification = classificationList[num]
        
	file1 = open(name_of_file, 'w')
 
	file1.write(tweetList[num])

	file1.close()
	
	try:
		os.rename('tweet'+str(num)+'.txt','C:\Conner\SENG474\dataMiningProject\classifications\\'+classificationList[num]+'\\'+'tweet'+str(num)+'.txt')
	except:
		print 'tweet'+str(num)+'.txt'
		print 'C:\Conner\SENG474\dataMiningProject\classifications\\'+classificationList[num]+'\\'+'tweet'+str(num)+'.txt'