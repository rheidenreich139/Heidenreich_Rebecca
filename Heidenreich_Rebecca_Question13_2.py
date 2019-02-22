import arcpy
from arcpy import env

gdbLocation= r'C:\gisclass\GIS610_Exercise3\Question_13.gdb'
logFileLocation = r'C:\gisclass\GIS610_Exercise3\Question 13\Question 13.txt'

arcpy.env.workspace = r"C:\gisclass\GIS610_Exercise3\Question 13\Question 13"
# Set local variables
inFeatures = ['tl_2018_04_tract.shp','tl_2018_us_county.shp']
outLocation = gdbLocation

# Execute TableToGeodatabase
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)


arcpy.env.workspace = r'C:\gisclass\GIS610_Exercise3\Question_13.gdb'

inFeatures = r"tl_2018_us_county"
outLocation = r"C:\gisclass\GIS610_Exercise3\Question_13.gdb"
outFeatureClass = r"Maricopa"

where_clause = "NAME = 'Maricopa'"
 
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, where_clause)

print('created')

# Set local variables
in_features = "tl_2018_04_tract"
clip_features = "Maricopa"
out_feature_class = r"C:\gisclass\GIS610_Exercise3\Question_13.gdb\Maricopa_Clip"
#xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis('tl_2018_04_tract', 'Maricopa', out_feature_class)

print("clipped")
