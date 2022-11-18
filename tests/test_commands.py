import os.path
from tempfile import TemporaryDirectory

import pystac
from stactools.testing import CliTestCase

from stactools.cop_dem import commands
from tests import test_data


class CreateItemTest(CliTestCase):

    def create_subcommand_functions(self):
        return [commands.create_cop_dem_command]

    def test_create_item(self):
        infile = test_data.get_external_data(
            "Copernicus_DSM_COG_10_N53_00_W115_00_DEM.tif")
        with TemporaryDirectory() as temporary_directory:
            outfile = os.path.join(temporary_directory, "item.json")
            args = ["cop-dem", "create-item", infile, outfile]
            result = self.run_command(args)
            self.assertEqual(result.exit_code, 0)
            item = pystac.read_file(outfile)
            item.validate()

    def test_create_collection(self):
        # TODO: add test for collection creation
        pass
