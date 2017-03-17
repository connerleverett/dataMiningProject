
import xlrd
import datetime
import xlsxwriter
import os
import sys


#Excel sheet which is being read
book = xlrd.open_workbook(r'C:\Conner\SENG474\allTweets.xlsx')
first_sheet=book.sheet_by_index(0)

#Excel Sheet which is being written to
workbook = xlsxwriter.Workbook('classifiedTweets.xlsx')

#Adding a worksheet to the workbook
worksheet=workbook.add_worksheet()

#Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

#Creating titles for the worksheet
worksheet.write(0,0,'Latitude',bold)
worksheet.write(0,1,'Longitude',bold)
worksheet.write(0,2,'Text',bold)
worksheet.write(0,3,'Hashtags',bold)
worksheet.write(0,4,'4 Classification',bold)
worksheet.write(0,5,'NS Classification',bold)
worksheet.write(0,6,'WE Classification',bold)

west = [[-124.0643428432363,21.62428133333164],[-96.00772959513533,23.79947308047025],[-96.80590076399045,53.98040411022095],[-134.3258179227266,47.91450808788012],[-124.0643428432363,21.62428133333164]]
east = [[-96.07939121667101,23.89136242112505],[-74.93897302251803,22.47292878157281],[-63.39544943013702,48.4429493189926],[-96.80590076399045,53.98040411022095],[-96.07939121667101,23.89136242112505]]
north = [[-125.6449664938869,38.66197668627194],[-71.58090383156198,35.47229043853898],[-64.79151011618875,46.75938227160562],[-129.0750507542309,49.55071476740098],[-125.6449664938869,38.66197668627194]] 
south = [[-122.5086591375994,24.83268060069677],[-77.553820419304,23.2546129052365],[-71.791595502684,35.52931696891457],[-125.5523513682803,38.74755487206231],[-122.5086591375994,24.83268060069677]]
 

####This code was found here: http://geospatialpython.com/2011/01/point-in-polygon.html and was not written by Conner Leverett
def point_in_poly(x,y,poly):
# Determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs (where x is the longitude and y is the latitude). 
#This function returns True or False.  
#The algorithm is called the "Ray Casting Method".
	n = len(poly)
	inside = False

	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xints:
						inside = not inside
		p1x,p1y = p2x,p2y
	return inside


nw = 0
ne = 0
sw = 0
se = 0
n = 0
s = 0
w = 0
e = 0
	
for row in range(1, first_sheet.nrows):	
	latitude = first_sheet.cell(row,1).value
	longitude = first_sheet.cell(row,2).value
	tweet = first_sheet.cell(row,4).value.encode('utf-8')
	hashtags = first_sheet.cell(row,6).value.encode('utf-8')
	
	westBool = point_in_poly(longitude, latitude, west)
	eastBool = point_in_poly(longitude, latitude, east)
	northBool = point_in_poly(longitude, latitude, north)
	southBool = point_in_poly(longitude, latitude, south)
	
	worksheet.write(row,0,latitude)
	worksheet.write(row,1,longitude)
	worksheet.write(row, 2, tweet.decode('utf-8'))
	worksheet.write(row,3,hashtags.decode('utf-8'))

	
	if (northBool):
		n+=1
		#north
		worksheet.write(row,5,0)
		if (westBool):
			#northwest
			worksheet.write(row, 4, 0)
			nw+=1
			#west
			worksheet.write(row, 6, 0)
			w+=1
		else:
			#northeast
			worksheet.write(row, 4, 1)
			ne+=1
			#east
			worksheet.write(row, 6, 1)
			e+=1
			
	if (southBool):
		s+=1
		#south
		worksheet.write(row, 5, 1)
		if (westBool):
			#southwest
			worksheet.write(row, 4, 3)
			sw+=1
			#west
			worksheet.write(row, 6, 0)
			w+=1
		else:
			#southeast
			worksheet.write(row, 4, 2)
			se+=1
			#east
			worksheet.write(row, 6, 1)
			e+=1
		
worksheet.write(0, 10, "Northwest")
worksheet.write(1, 10, nw)
worksheet.write(0, 11, "Northeast")
worksheet.write(1, 11, ne)
worksheet.write(0, 12, "Southwest")
worksheet.write(1, 12, sw)
worksheet.write(0, 13, "Southeast")
worksheet.write(1, 13, se)

worksheet.write(0, 14, "North")
worksheet.write(1, 14, n)
worksheet.write(0, 15, "South")
worksheet.write(1, 15, s)
worksheet.write(0, 16, "West")
worksheet.write(1, 16, w)
worksheet.write(0, 17, "East")
worksheet.write(1, 17, e)
	
#This is needed to save the excel file
workbook.close()	