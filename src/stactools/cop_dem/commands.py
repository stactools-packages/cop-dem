import click

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

    return cop_dem
