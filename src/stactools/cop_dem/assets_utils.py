"""
Creates the Item Assets section
"""
import os.path
from typing import Tuple


def change_asset_directory(href: str, asset_name: str,
                           subdirectory: str) -> Tuple[str, str]:
    """
    Apply a subdirectory prefix, and ensure the correct capitalization of files.
    """
    asset_href = os.path.join(os.path.dirname(href), subdirectory,
                              os.path.basename(href))

    asset_href = asset_href.replace("DEM.tif", asset_name)

    return (asset_name[:-4].lower(), asset_href)
