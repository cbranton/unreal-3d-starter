# export_assets.py

import unreal


def exportSelectedAssets():
    """
    Exports the selected mesh assets as FBX file.
    """
    # TODO: use relative paths
    full_path = "C:\\Users\\cbranton\\Documents\\ExportedAssets"
    
    # get the selected assets
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    print ("Selected assets are", selected_assets)

    for asset in selected_assets:
        asset_name = asset.get_name()
        print ("Asset name is", asset_name)
        # create asset export task
        export_task = unreal.AssetExportTask()
        export_task.automated = True
        export_task.filename = full_path + asset_name + '.fbx'
        print ("Object being written to", export_task.filename)
        export_task.object = asset
        export_task.options = unreal.FbxExportOption()
        export_task.prompt = False


        # create class specific exporter
        fbx_exporter = unreal.StaticMeshExporterFBX()
        export_task.exporter = fbx_exporter
        fbx_exporter.run_asset_export_task(export_task)
        print ("Export complete")

print ("hello again")
exportSelectedAssets()
