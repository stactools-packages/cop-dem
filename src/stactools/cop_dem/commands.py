import click
import os

from stactools.cop_dem import stac


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
    def create_item_command(source, destination, validate):
        item = stac.create_item(source)
        if validate:
            item.validate()
        item.save_object(dest_href=destination)

    @cop_dem.command("create-collection",
                     short_help="Creates a STAC Collection for Copernicus DEM."
                     )
    @click.argument("product")
    @click.argument("destination")
    @click.option("-u",
                  "--url",
                  default='',
                  type=str,
                  help="Root url to prepend to all records")
    @click.option("--validate/--no-validate",
                  default=True,
                  help="Validate the item before saving")
    def create_collection_command(destination: str, product: str, url: str,
                                  validate: bool):
        """ Creates a STAC Collection

        Args:
        product: The DEM product, glo30 or glo90

        """
        collection = stac.create_collection(product)
        json_path = os.path.join(destination, f'{collection.id}.json')
        collection.set_self_href(
            os.path.join(url, collection.id, os.path.basename(json_path)))
        if validate:
            collection.validate()
        collection.save_object(dest_href=json_path)

    return cop_dem
