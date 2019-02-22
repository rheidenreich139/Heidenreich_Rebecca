#Question 12.Retrieve records from the GeneralOffense feature class which meet the following criteria:
#a.	Return only records that has the OffenseCus = BURGLARY FORCE and have its field locationTranslation = Residence/Home
#Finally, write the results to a CSV file.

import arcpy
import csv

featureClass = r'C:\gisclass\GIS610_Exercise3\Exercise 3.gdb\General_Offense'

fieldNames = ['OffenseCustom', 'locationTranslation']
cursorFields = ','.join(fieldNames)
crimeCount = 0

filterStatement = "OffenseCustom = 'BURGLARY FORCE' AND locationTranslation = 'Residence/Home'"

with open('Burg_Res.csv','w') as csvFile:
	fileWriter = csv.writer(csvFile,delimiter = ',',quotechar = '|', quoting = csv.QUOTE_MINIMAL)
	fileWriter.writerow(fieldNames)
	with arcpy.da.SearchCursor(featureClass,fieldNames,filterStatement) as cursor:
		for row in cursor:
			crimeCount += 1
			fileWriter.writerow(row)

print('CSV Created')
