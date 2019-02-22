#Question 8. Return the count of records in the CallsforService feature class

import arcpy
 
lyrfile = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb\CallsforService.lyr"
result = arcpy.GetCount_management(lyrfile)
count = int(result.getOutput(0))
print(count)
