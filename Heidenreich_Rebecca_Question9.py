#Question 9.Create a feature class (you may re-use the geodatabase from Question 5). 
#Add a field to your feature class. Then add a domain to the just created field. Finally, add at least 5 values to your domain. (*Your domain may be of any type)

import arcpy
arcpy.env.workspace = r"C:\gisclass\GIS610_Exercise3\exercise3GDB.gdb"
arcpy.env.overwriteOutput = True

out_path = r"C:\gisclass\GIS610_Exercise3\exercise3GDB.gdb"
out_name = r"Trees"
geometry_type = r"POINT"
template = r"Rivers"
has_m = r"DISABLED"
has_z = r"DISABLED"

spatial_ref = arcpy.Describe(r"C:\gisclass\GIS610_Exercise3\exercise3GDB.gdb\Rivers").spatialReference
arcpy.CreateFeatureclass_management( out_path, out_name, geometry_type, template, 
                                    has_m, has_z, spatial_ref)

inFeatures = "Trees"
fieldName1 = "TreeTypes"
fieldPrecision = 9
fieldAlias = "TreeTypes"

arcpy.AddField_management(inFeatures, fieldName1, "TEXT", fieldPrecision,
                          field_alias=fieldAlias)

domName = r"Environment"
gdb = arcpy.env.workspace
inFeatures = r"C:\gisclass\GIS610_Exercise3\exercise3GDB.gdb\Trees"
inField = r"TreeTypes"
arcpy.CreateDomain_management(gdb, domName, "Tree Environment", 
                              "TEXT", "CODED")

domDict = {"CD":"Cold desert", "HD": "Hot desert", "WOL": "Woodland", 
           "WEL": "Wetland", "AM": "Arid mountain"}

for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

arcpy.AssignDomainToField_management(inFeatures, inField, domName)
print('everythings fine')
