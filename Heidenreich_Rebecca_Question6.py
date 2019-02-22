#Question6. Using the CallsforService feature class that you’ve been given, add a field called
#‘Crime_Explanation’ with the data type Text/String. Then, if the value of field ‘CFSType’ is
#Burglary Call, write ‘This is a burglary’ into the field that you just added.
import arcpy
 
arcpy.env.workspace = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb"
arcpy.env.overwriteOutput = True
inFeatures = r"CallsforService"
fieldName = r"Crime_Explanation"
fieldLength = 50
arcpy.AddField_management(inFeatures, fieldName, "TEXT")
print('added field')
#featureClass = r"CallsforService"

fieldNames = ['CFSType','Crime_Explanation']

with arcpy.da.UpdateCursor(inFeatures, fieldNames) as cursor:
    for x in cursor:
        if x[0] == ('Burglary Call'):
           x[1] = 'This is a burglary'
           cursor.updateRow(x)