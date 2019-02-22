#Question 5. Create a geodatabase. Then, using the following list, generate feature classes for each of the
#elements in the list: featureList = [‘CapitalCities’, ‘Landmarks’, ‘HistoricPlaces’, ‘StateNames’, ‘Nationalities’,‘Rivers’]
import arcpy
out_folder_path = r"C:\gisclass\GIS610_Exercise3" 
out_name = "exercise3GDB.gdb"
arcpy.env.overwriteOutput = True
arcpy.CreateFileGDB_management(r'C:\gisclass\GIS610_Exercise3', 'exercise3GDB.gdb')


current_workspace = r'C:\gisclass\GIS610_Exercise3\exercise3GDB.gdb'

geometry_type = 'POINT'

spatial_reference = arcpy.SpatialReference(102100)

featureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities','Rivers']

arcpy.env.workspace = current_workspace


def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)

    print('Feature Class ' + in_fc_name + ' was sucessfully created.')


filteredFeatureClassNameList = [fc for fc in featureClassNamesList if fc.startswith("A")]

print(filteredFeatureClassNameList)

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

print('All Done')
