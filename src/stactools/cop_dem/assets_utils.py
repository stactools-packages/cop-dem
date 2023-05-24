"""
Creates the Item Assets section
"""
from urllib.parse import urljoin
from typing import Tuple


def change_asset_directory(*, href: str, asset_name: str,
                           subdirectory: str) -> Tuple[str, str]:
    """
    Apply a subdirectory prefix, and ensure the correct capitalization of files.
    """
    _, basename = href.rsplit('/', 1)
    asset_href = urljoin(href, f"{subdirectory}/{basename}")
    asset_href = asset_href.replace("DEM.tif", asset_name)

    return (asset_name[:-4].lower(), asset_href)
