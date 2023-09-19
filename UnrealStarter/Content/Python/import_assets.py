'''
Note: when working with assets, use the unreal.EditorAssetLibrary API,
rather than built-in Python file handling functions.
'''

import unreal

def import_assets():
    # TODO: work on a better way to set up a source path
    source_folder = "C:\\Users\\cbranton\\Documents\\AssetsImport\\"
    file_names = [
        source_folder + "Revan_Lightsaber.fbx"
#        source_folder + "TrussGame-Geometry.FBX"
    ]
    print(file_names)

    # create asset tools
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # create an asset import data object and set attributes
    asset_import_data = unreal.AutomatedAssetImportData()
    asset_import_data.destination_path = '/Game/Meshes/ImportTest'
    asset_import_data.filenames = file_names
    asset_tools.import_assets_automated(asset_import_data)

import_assets()