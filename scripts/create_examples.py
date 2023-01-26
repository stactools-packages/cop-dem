#!/usr/bin/env python3

from pathlib import Path

from pystac import CatalogType

from stactools.cop_dem import stac

root = Path(__file__).parents[1]
examples = root / "examples"
tiles = root / "tests" / "data-files" / "external"


def gen_collection_example(collection_name):
    collection = stac.create_collection(collection_name)
    aa = int(str.split(collection_name, "-")[1]) // 3
    items = [stac.create_item([str(p) for p in tiles.glob(f"*{aa}*.tif")][0])]
    collection.add_items(items)

    collection.normalize_hrefs(str(examples))
    collection.make_all_asset_hrefs_relative()
    json_path = examples / f"cop-dem-{collection_name}"
    collection.save(dest_href=json_path.as_posix(),
                    catalog_type=CatalogType.SELF_CONTAINED)


gen_collection_example("glo-30")
gen_collection_example("glo-90")
