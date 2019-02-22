#Question 10. Perform a spatial join between the census tracts feature class and the general offense feature class.

import arcpy
arcpy.env.overwriteOutput = True

target_features = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb\General_Offense"
join_features = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb\Tracts"
out_feature_class = r"C:\gisclass\GIS610_Exercise3\Exercise 3.gdb\General_Offense_Tracts"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)