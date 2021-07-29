import os.path
import re
from typing import Optional
from pystac.asset import Asset
from pystac.extensions.projection import ProjectionExtension
from pystac.media_type import MediaType

import rasterio
from shapely.geometry import mapping, box
from pystac import Item

from stactools.core.io import ReadHrefModifier
from stactools.cop_dem.constants import (COP_DEM_LINKS, COP_DEM_PROVIDERS,
                                         OPENTOPOGRAPHY_DATETIME,
                                         COP_DEM_PLATFORM, COP_DEM_EPSG)


def create_item(href: str,
                read_href_modifier: Optional[ReadHrefModifier] = None) -> Item:
    """Creates a STAC Item from a single tile of ALOS DEM data."""
    if read_href_modifier:
        modified_href = read_href_modifier(href)
    else:
        modified_href = href
    with rasterio.open(modified_href) as dataset:
        if dataset.crs.to_epsg() != COP_DEM_EPSG:
            raise ValueError(
                f"Dataset {href} is not EPSG:{COP_DEM_EPSG}, which is required for ALOS DEM data"
            )
        bbox = list(dataset.bounds)
        geometry = mapping(box(*bbox))
        transform = dataset.transform
        shape = dataset.shape
        item = Item(id=os.path.splitext(os.path.basename(href))[0],
                    geometry=geometry,
                    bbox=bbox,
                    datetime=OPENTOPOGRAPHY_DATETIME,
                    properties={},
                    stac_extensions={})

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

    item.add_links(COP_DEM_LINKS)
    item.common_metadata.platform = COP_DEM_PLATFORM
    item.common_metadata.gsd = gsd
    item.common_metadata.providers = COP_DEM_PROVIDERS
    item.common_metadata.license = "proprietary"

    item.add_asset(
        "data",
        Asset(href=href,
              title=title,
              description=None,
              media_type=MediaType.COG,
              roles=["data"]))

    projection = ProjectionExtension.ext(item, add_if_missing=True)
    projection.epsg = COP_DEM_EPSG
    projection.transform = transform[0:6]
    projection.shape = shape

    return item
