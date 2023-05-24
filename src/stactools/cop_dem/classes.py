
[
{'name': 'Void_(no_data)', 'value': 0, 'description': 'Void (no data)'}
{'name': 'Not_edited', 'value': 1, 'description': 'Not edited'}
{'name': 'Infill_of_external_elevation_data', 'value': 2, 'description': 'Infill of external elevation data'}
{'name': 'Interpolated_pixels', 'value': 3, 'description': 'Interpolated pixels'}
{'name': 'Smoothed_pixels', 'value': 4, 'description': 'Smoothed pixels'}
{'name': 'Airport_editing', 'value': 5, 'description': 'Airport editing'}
{'name': 'Raised_negative_elevation_pixels', 'value': 6, 'description': 'Raised negative elevation pixels'}
{'name': 'Flattened_pixels', 'value': 7, 'description': 'Flattened pixels'}
{'name': 'Ocean_pixels', 'value': 8, 'description': 'Ocean pixels'}
{'name': 'Lake_pixels', 'value': 9, 'description': 'Lake pixels'}
{'name': 'River_pixels', 'value': 10, 'description': 'River pixels'}
{'name': 'Shoreline_pixels', 'value': 11, 'description': 'Shoreline pixels'}
{'name': 'Morphed_pixels_(series_of_pixels_manually_set)', 'value': 12, 'description': 'Morphed pixels (series of pixels manually set)'}
{'name': 'Shifted_pixels', 'value': 13, 'description': 'Shifted pixels'}
]



FLM_classes = [
    {'name': 'Void_(no_data)', 'value': 0, 'description': 'Void (no data)'}
    {'name': 'Edited_(except_filled_pixels)', 'value': 1, 'description': 'Edited (except filled pixels)'}
    {'name': 'Not_edited_/_not_filled', 'value': 2, 'description': 'Not edited / not filled'}
    {'name': 'ASTER', 'value': 3, 'description': 'ASTER'}
    {'name': 'SRTM90', 'value': 4, 'description': 'SRTM90'}
    {'name': 'SRTM30', 'value': 5, 'description': 'SRTM30'}
    {'name': 'GMTED2010', 'value': 6, 'description': 'GMTED2010'}
    {'name': 'SRTM30plus', 'value': 7, 'description': 'SRTM30plus'}
    {'name': 'TerraSAR-X_Radargrammetric_DEM', 'value': 8, 'description': 'TerraSAR-X Radargrammetric DEM'}
    {'name': 'AW3D306', 'value': 9, 'description': 'AW3D306'}
    {'name': 'Norway_DEM', 'value': 100, 'description': 'Norway DEM'}
    {'name': 'DSM05_Spain', 'value': 101, 'description': 'DSM05 Spain'}
    {'name': 'Norway_DEM_v2', 'value': 102, 'description': 'Norway DEM v2'}
]



WBM_classes = [
    {'name': 'No_water', 'value': 0, 'description': 'No water'}
    {'name': 'Ocean', 'value': 1, 'description': 'Ocean'}
    {'name': 'Lake', 'value': 2, 'description': 'Lake'}
    {'name': 'River', 'value': 3, 'description': 'River'}
]




def dict2dict(dict):
    for key, value in dict.items(): 
        new_dict = {"name":value.replace(" ","_"),"value":key, "description": value}
        print(new_dict)


EDM = {    
    0: "Void (no data)",
    1: "Not edited",
    2: "Infill of external elevation data",
    3: "Interpolated pixels",
    4: "Smoothed pixels",
    5: "Airport editing",
    6: "Raised negative elevation pixels",
    7: "Flattened pixels",
    8: "Ocean pixels",
    9: "Lake pixels",
    10: "River pixels",
    11: "Shoreline pixels",
    12: "Morphed pixels (series of pixels manually set)",
    13: "Shifted pixels",
}

WBM = {
    0: "No water",
    1: "Ocean",
    2: "Lake",
    3: "River"
}

FLM = {
    0: "Void (no data)",
    1: "Edited (except filled pixels)",
    2: "Not edited / not filled",
    3: "ASTER",
    4: "SRTM90",
    5: "SRTM30",
    6: "GMTED2010",
    7: "SRTM30plus",
    8: "TerraSAR-X Radargrammetric DEM",
    9: "AW3D306",
    100: "Norway DEM",
    101: "DSM05 Spain",
    102: "Norway DEM v2",
}