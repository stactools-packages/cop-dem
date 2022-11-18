import os.path
import re
from typing import Optional
# from pystac.asset import Asset
from pystac import (Collection, Extent, Asset, Summaries, SpatialExtent,
                    TemporalExtent)
from pystac.extensions.projection import ProjectionExtension
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.raster import RasterExtension
from pystac.media_type import MediaType

import rasterio
from shapely.geometry import mapping, box
from pystac import Item

from stactools.core.io import ReadHrefModifier
from stactools.cop_dem import constants as co


def create_item(href: str,
                read_href_modifier: Optional[ReadHrefModifier] = None) -> Item:
    """Creates a STAC Item from a single tile of Copernicus DEM data."""
    if read_href_modifier:
        modified_href = read_href_modifier(href)
    else:
        modified_href = href
    with rasterio.open(modified_href) as dataset:
        if dataset.crs.to_epsg() != co.COP_DEM_EPSG:
            raise ValueError(f"Dataset {href} is not EPSG:{co.COP_DEM_EPSG}, "
                             "which is required for Copernicus DEM data")
        bbox = list(dataset.bounds)
        geometry = mapping(box(*bbox))
        transform = dataset.transform
        shape = dataset.shape
        item = Item(id=os.path.splitext(os.path.basename(href))[0],
                    geometry=geometry,
                    bbox=bbox,
                    datetime=co.COP_DEM_COLLECTION_START,
                    properties={},
                    stac_extensions=[])

    p = re.compile(r'Copernicus_DSM_COG_(\d\d)_(.*)_DEM.tif')
    m = p.match(os.path.basename(href))
    if m:
        if m.group(1) == '30':
            gsd = 90
        elif m.group(1) == '10':
            gsd = 30
        else:
            raise ValueError("unknown resolution {}".format(m.group(1)))
        title = m.group(2)
    else:
        raise ValueError("unable to parse {}".format(href))

    item.add_links(co.COP_DEM_LINKS)
    item.common_metadata.platform = co.COP_DEM_PLATFORM
    item.common_metadata.gsd = gsd
    item.common_metadata.providers = co.COP_DEM_PROVIDERS
    item.common_metadata.license = "proprietary"

    item.add_asset(
        "data",
        Asset(href=href,
              title=title,
              description=None,
              media_type=MediaType.COG,
              roles=["data"]))

    projection = ProjectionExtension.ext(item, add_if_missing=True)
    projection.epsg = co.COP_DEM_EPSG
    projection.transform = transform[0:6]
    projection.shape = shape

    return item


def create_collection(product: str) -> Collection:
    """Create a STAC Collection

    This function includes logic to extract all relevant metadata from
    an asset describing the STAC collection and/or metadata coded into an
    accompanying constants.py file.

    See `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_.

    Args:
        Product (str): glo-30 or glo-90

    Returns:
        Item: STAC Item object

    Returns:
        Collection: STAC Collection object
    """
    if product == "glo-30":
        summaries = {
            "gsd": 30,
            "platform": co.COP_DEM_PLATFORM,
            # "instruments": ,
        }
    elif product == "glo-90":
        summaries = {
            "gsd": 90,
            "platform": co.COP_DEM_PLATFORM,
            # "instruments": ,
        }
    else:
        {
            # TODO: Raise and error no matching product
        }

    # TODO: Stub, Fill in actual collection information
    collection = Collection(
        id=f"cop-dem-{product}",
        title="",
        description="",
        license="proprietary",
        providers=co.COP_DEM_PROVIDERS,  # TODO how to vary the host
        keywords=['DEM', 'COPERNICUS'],
        # catalog_type=
        summaries=Summaries(summaries),
        extent=Extent(SpatialExtent(co.COP_DEM_SPATIAL_EXTENT),
                      TemporalExtent([co.COP_DEM_TEMPORAL_EXTENT])),
        stac_extensions=[
            ItemAssetsExtension.get_schema_uri(),
            ProjectionExtension.get_schema_uri(),
            RasterExtension.get_schema_uri(),
        ])

    assets = ItemAssetsExtension.ext(collection, add_if_missing=True)
    assets.item_assets = co.COP_DEM_ASSETS

    return collection
