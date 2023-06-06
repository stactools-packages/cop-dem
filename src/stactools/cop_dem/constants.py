from datetime import datetime
from typing import Optional

from pystac import Provider, Link, ProviderRole
from pystac.extensions.item_assets import AssetDefinition
from pystac.extensions.raster import DataType
from pystac.utils import str_to_datetime
from pystac.media_type import MediaType
from stactools.cop_dem.classes import EDM_classes, FLM_classes, WBM_classes

CLASSIFICATION_EXTENSION_SCHEMA = "https://stac-extensions.github.io/classification/v1.1.0/schema.json"  # noqa:E501

UINT8_BAND = [{"data_type": DataType.UINT8}]

FLOAT32_BAND = [{"data_type": DataType.FLOAT32}]

COP_DEM_PRODUCTS = ['glo-30', 'glo-90']

COP_DEM_SPATIAL_EXTENT = [[-180., -90., 180., 90.]]

COP_DEM_COLLECTION_START: Optional[datetime] = str_to_datetime(
    "2021-04-22T00:00:00Z")

COP_DEM_COLLECTION_END: Optional[datetime] = str_to_datetime(
    "2021-04-22T00:00:00Z")

COP_DEM_TEMPORAL_EXTENT = [COP_DEM_COLLECTION_START,
                           COP_DEM_COLLECTION_END]  # TODO: find the dates

COP_DEM_PLATFORM = "tandem-x"

COP_DEM_EPSG = 4326

COP_DEM_KEYWORDS = ['DEM', 'COPERNICUS', 'DSM', 'Elevation']

COP_DEM_PROVIDERS = [
    Provider("European Space Agency",
             roles=[ProviderRole.LICENSOR],
             url=("https://spacedata.copernicus.eu/documents/20126/0/"
                  "CSCDA_ESA_Mission-specific+Annex.pdf")),
    Provider("Sinergise",
             roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
             url="https://registry.opendata.aws/copernicus-dem/"),
]

# Various HOST options
COP_DEM_HOST = {
    "OT":
    Provider("OpenTopography",
             roles=[ProviderRole.HOST],
             url=("https://portal.opentopography.org/"
                  "datasetMetadata?otCollectionID=OT.032021.4326.1")),
    "AWS":
    Provider("Sinergise",
             roles=[ProviderRole.HOST],
             url="https://registry.opendata.aws/copernicus-dem/")
}

COP_DEM_LINKS = [
    Link(
        "handbook",
        "https://object.cloud.sdsc.edu/v1/AUTH_opentopography/www/metadata/Copernicus_metadata.pdf",
        "application/pdf",
        "Copernicus DEM User handbook",
        extra_fields={"description": "Also includes data usage information"}),
    Link(
        "product handbook",
        "https://spacedata.copernicus.eu/documents/20123/122407/GEO1988-CopernicusDEM-SPE-002_ProductHandbook_I5.0+%281%29.pdf/706ee17d-2cce-f1fa-a73e-1686d28f09dd?t=1679657087883"  # noqa: E501
        "application/pdf",
        "Copernicus DEM Product Handbook (Nov 2022)",
        extra_fields={"description": "Also includes data usage information"}),
    Link(
        "license",
        "https://spacedata.copernicus.eu/documents/20123/121286/CSCDA_ESA_Mission-specific+Annex_31_Oct_22.pdf",  # noqa: E501
        "Copernicus Data Access")
]

COP_DEM_ASSETS = {
    "data":
    AssetDefinition({
        "type": MediaType.COG,
        "roles": ["data"],
    }),
    "edm":
    AssetDefinition({
        "title": "Editing Mask",
        "type": MediaType.COG,
        "description": "Editing Mask",
        "role": ["mask"],
        "raster:bands": UINT8_BAND,
        "classification:classes": EDM_classes,
    }),
    "flm":
    AssetDefinition({
        "title": "Filling Mask",
        "type": MediaType.COG,
        "description": "Filling Mask",
        "role": ["mask"],
        "raster:bands": UINT8_BAND,
        "classification:classes": FLM_classes,
    }),
    "wbm":
    AssetDefinition({
        "title": "Water Body Mask",
        "type": MediaType.COG,
        "description": "Water Body Mask",
        "role": ["mask"],
        "raster:bands": UINT8_BAND,
        "classification:classes": WBM_classes,
    }),
    "hem":
    AssetDefinition({
        "title": "Height Error Mask",
        "type": MediaType.COG,
        "description": "Height Error Mask",
        "role": ["mask"],
        "raster:bands": FLOAT32_BAND,
    }),
    "acm":
    AssetDefinition({
        "title": "Accuracy Layer",
        "type": "application/vnd.google-earth.kml+xml",
        "description": "Accuracy Layer",
        "role": ["mask"],
    }),
    "src":
    AssetDefinition({
        "title": "Source Mask",
        "type": "application/vnd.google-earth.kml+xml",
        "description": "Source Mask",
        "role": ["mask"],
    }),
    "dem_ql":
    AssetDefinition({
        "title": "DEM QuickLook Relative",
        "type": MediaType.GEOTIFF,
        "description":
        "QuickLook of Digital Elevation Model with shaded relief representation (relative)",
        "role": ["overview"],
    }),
    "ql":
    AssetDefinition({
        "title": "QuickLook KML",
        "type": "application/vnd.google-earth.kml+xml",
        "description": "KML of QuickLook data visualization",
        "role": ["overview"],
    }),
    "dem_abs_ql":
    AssetDefinition({
        "title": "DEM QuickLook Absolute",
        "type": MediaType.GEOTIFF,
        "description":
        "QuickLook of Digital Elevation Model with shaded relief representation (absolute)",
        "role": ["overview"],
    }),
    "edm_ql":
    AssetDefinition({
        "title": "Editing Mask QuickLook",
        "type": MediaType.GEOTIFF,
        "description": "QuickLook of Editing Mask",
        "role": ["overview"],
    }),
    "flm_ql":
    AssetDefinition({
        "title": "Filling Mask QuickLook",
        "type": MediaType.GEOTIFF,
        "description": "QuickLook of Filling Mask",
        "role": ["overview"],
    }),
    "wbm_ql":
    AssetDefinition({
        "title": "Water Body Mask QuickLook",
        "type": MediaType.GEOTIFF,
        "description": "QuickLook of Water Body Mask",
        "role": ["overview"],
    }),
    "hem_ql":
    AssetDefinition({
        "title": "Height Error Mask QuickLook",
        "type": MediaType.GEOTIFF,
        "description": "QuickLook of Height Error Mask",
        "role": ["overview"],
    }),
}

COP_DEM_DESCRIPTION = '''The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. We provide two instances of Copernicus DEM named GLO-30 Public and GLO-90. GLO-90 provides worldwide coverage at 90 meters. GLO-30 Public provides limited worldwide coverage at 30 meters because a small subset of tiles covering specific countries are not yet released to the public by the Copernicus Programme. Note that in both cases ocean areas do not have tiles, there one can assume height values equal to zero. Data is provided as Cloud Optimized GeoTIFFs and comes from Copernicus DEM 2021 release.'''  # noqa: E501
