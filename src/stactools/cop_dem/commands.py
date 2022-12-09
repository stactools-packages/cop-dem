import click
import os

from stactools.cop_dem import stac
from stactools.cop_dem import constants as co


def create_cop_dem_command(cli):
    """Creates the COP DEM stactools commands."""

    @cli.group("cop-dem", short_help="Work with Copernicus DEM data.")
    def cop_dem():
        pass

    @cop_dem.command(
        "create-item",
        short_help="Creates a STAC item from an Copernicus DEM tile.")
    @click.argument("source")
    @click.argument("destination")
    @click.option("--validate/--no-validate",
                  default=True,
                  help="Validate the item before saving")
    @click.option("--host",
                  type=click.Choice(co.COP_DEM_HOST.keys(),
                                    case_sensitive=False),
                  default=None,
                  help="Set PROVIDER HOST")
    def create_item_command(source: str, destination: str, validate: bool,
                            host: str):
        """ Creates a STAC Collection

        source: Path to input item

        destination: Folder to output json

        """
        item = stac.create_item(source, host=host)
        if validate:
            item.validate()
        item.save_object(dest_href=destination)

    @cop_dem.command("create-collection",
                     short_help="Creates a STAC Collection for Copernicus DEM."
                     )
    @click.argument("product", type=click.Choice(['glo-30', 'glo-90']))
    @click.argument("destination", type=click.Path(exists=True))
    @click.option("-u",
                  "--url",
                  default='',
                  type=str,
                  help="Root url to prepend to all records")
    @click.option("--validate/--no-validate",
                  default=True,
                  help="Validate the item before saving")
    @click.option("--host",
                  type=click.Choice(co.COP_DEM_HOST.keys(),
                                    case_sensitive=False),
                  default=None,
                  help="Set PROVIDER HOST")
    def create_collection_command(destination: str, product: str, url: str,
                                  validate: bool, host: str):
        """ Creates a STAC Collection

        product: The DEM product, glo-30 or glo-90

        destination: Folder to output json

        """
        collection = stac.create_collection(product, host=host)
        json_path = os.path.join(destination, f'{collection.id}.json')
        collection.set_self_href(
            os.path.join(url, collection.id, os.path.basename(json_path)))
        if validate:
            collection.validate()
        collection.save_object(dest_href=json_path)

    return cop_dem
