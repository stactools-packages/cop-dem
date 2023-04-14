from stactools.testing import TestData

test_data = TestData(
    __file__,
    {
        "Copernicus_DSM_COG_10_N53_00_W115_00_DEM.tif": {
            "url": "s3://raster/COP30/COP30_hh/Copernicus_DSM_COG_10_N53_00_W115_00_DEM.tif",
            "s3": {
                "anon": True,
                "client_kwargs": {
                    "endpoint_url": "https://opentopography.s3.sdsc.edu",
                },
            },
        },
        "Copernicus_DSM_COG_30_N53_00_W115_00_DEM.tif": {
            "url": "s3://raster/COP90/COP90_hh/Copernicus_DSM_COG_30_N53_00_W115_00_DEM.tif",
            "s3": {
                "anon": True,
                "client_kwargs": {
                    "endpoint_url": "https://opentopography.s3.sdsc.edu",
                },
            },
        },
    },
)
