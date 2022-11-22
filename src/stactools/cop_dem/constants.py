from datetime import datetime
from typing import Optional

from pystac import Provider, Link, ProviderRole
from pystac.extensions.item_assets import AssetDefinition
from pystac.utils import str_to_datetime
from pystac.media_type import MediaType

COP_DEM_SPATIAL_EXTENT = [[-180., -90., 180., 90.]]
COP_DEM_COLLECTION_START: Optional[datetime] = str_to_datetime(
    "2021-04-22T00:00:00Z")
COP_DEM_COLLECTION_END: Optional[datetime] = str_to_datetime(
    "2021-04-22T00:00:00Z")
COP_DEM_TEMPORAL_EXTENT = [COP_DEM_COLLECTION_START,
                           COP_DEM_COLLECTION_END]  # TODO: find the dates
COP_DEM_PLATFORM = "TanDEM-X"
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
        "license",
        "https://spacedata.copernicus.eu/documents/20126/0/CSCDA_ESA_Mission-specific+Annex.pdf",
        "Copernicus Data Access")
]

COP_DEM_ASSETS = {
    "data": AssetDefinition({
        "type": MediaType.COG,
        "roles": ["data"],
    })
}

COP_DEM_DESCRIPTION = '''The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. We provide two instances of Copernicus DEM named GLO-30 Public and GLO-90. GLO-90 provides worldwide coverage at 90 meters. GLO-30 Public provides limited worldwide coverage at 30 meters because a small subset of tiles covering specific countries are not yet released to the public by the Copernicus Programme. Note that in both cases ocean areas do not have tiles, there one can assume height values equal to zero. Data is provided as Cloud Optimized GeoTIFFs and comes from Copernicus DEM 2021 release.'''  # noqa: E501
