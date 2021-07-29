import datetime

from pystac import Provider, Link

COP_DEM_PLATFORM = "TanDEM-X"
COP_DEM_EPSG = 4326
COP_DEM_PROVIDERS = [
    Provider("European Space  Agency",
             roles=["licensor"],
             url=("https://spacedata.copernicus.eu/documents/20126/0/"
                  "CSCDA_ESA_Mission-specific+Annex.pdf")),
    Provider("Sinergise",
             roles=["producer", "processor"],
             url="https://registry.opendata.aws/copernicus-dem/"),
    Provider("OpenTopography",
             roles=["host"],
             url=("https://portal.opentopography.org/"
                  "datasetMetadata?otCollectionID=OT.032021.4326.1"))
]
COP_DEM_LINKS = [
    Link(
        "handbook",
        "https://object.cloud.sdsc.edu/v1/AUTH_opentopography/www/metadata/Copernicus_metadata.pdf",
        "application/pdf",
        "Copernicus DEM User handbook",
        extra_fields={"description": "Also includes data usage information"})
]

# This stactools package was created to interact with the Copernicus DEM data hosted
# on OpenTopography. As of this writing, the data were last updated at this
# time. This information was taken from
# https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.112016.4326.2.
OPENTOPOGRAPHY_DATETIME = datetime.datetime(2021,
                                            4,
                                            22,
                                            tzinfo=datetime.timezone.utc)
