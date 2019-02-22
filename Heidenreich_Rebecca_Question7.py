#Question7 Write Python code that selects a subset of the records from a given feature
#class and writes
#those features to a different feature class.  You may choose which feature
#class that your code uses.
import arcpy
arcpy.env.workspace = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

inFeatures = r"General_Offense"
outLocation = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb"
outFeatureClass = r"CallsforService_delimited"
#delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, "PLACE_NAME")
#expression = delimitedField + " = 'CallsforService'"
where_clause = "place_name = '201 WEST'"
 
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, where_clause)
