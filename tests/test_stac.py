import datetime
from unittest import TestCase

import pystac
from pystac import Provider, MediaType
from pystac.extensions.projection import ProjectionExtension
from pystac.extensions.raster import RasterExtension
from pystac.provider import ProviderRole

from stactools.cop_dem import stac

from tests import test_data


class StacTest(TestCase):

    def setUp(self):
        self.glo30_path = test_data.get_external_data(
            "Copernicus_DSM_COG_10_N53_00_W115_00_DEM.tif")
        self.glo90_path = test_data.get_external_data(
            "Copernicus_DSM_COG_30_N53_00_W115_00_DEM.tif")

    def test_create_glo30_item(self):
        item = stac.create_item(self.glo30_path)
        self.assertEqual(item.id, "Copernicus_DSM_COG_10_N53_00_W115_00_DEM")
        self.assertIsNotNone(item.geometry)
        self.assertEqual(list(item.bbox), [
            -115.00020833333333, 53.00013888888889, -114.00020833333333,
            54.00013888888889
        ])
        self.assertEqual(
            item.datetime,
            datetime.datetime(2021, 4, 22, tzinfo=datetime.timezone.utc))

        common_metadata = item.common_metadata
        self.assertEqual(common_metadata.platform, "tandem-x")
        self.assertEqual(common_metadata.gsd, 30)
        expected_providers = [
            Provider("European Space Agency",
                     roles=[ProviderRole.LICENSOR],
                     url=("https://spacedata.copernicus.eu/documents/20126/0/"
                          "CSCDA_ESA_Mission-specific+Annex.pdf")),
            Provider("Sinergise",
                     roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
                     url="https://registry.opendata.aws/copernicus-dem/"),
            Provider("OpenTopography",
                     roles=[ProviderRole.HOST],
                     url=("https://portal.opentopography.org/"
                          "datasetMetadata?otCollectionID=OT.032021.4326.1"))
        ]
        for expected, actual in zip(expected_providers,
                                    common_metadata.providers):
            self.assertDictEqual(expected.to_dict(), actual.to_dict())
        self.assertEqual(common_metadata.license, "proprietary")

        projection = ProjectionExtension.ext(item)
        self.assertEqual(projection.epsg, 4326)
        self.assertEqual(projection.shape, (3600, 2400))
        self.assertEqual(list(projection.transform), [
            0.00041666666666666664, 0.0, -115.00020833333333, 0.0,
            -0.0002777777777777778, 54.00013888888889
        ])

        handbook = item.get_single_link("handbook")
        self.assertIsNotNone(handbook)
        self.assertEqual(handbook.title, "Copernicus DEM User handbook")
        self.assertEqual(handbook.rel, "handbook")
        self.assertEqual(
            handbook.href,
            "https://object.cloud.sdsc.edu/v1/AUTH_opentopography/www/metadata"
            "/Copernicus_metadata.pdf")
        self.assertEqual(handbook.media_type, "application/pdf")

        data = item.assets["data"]
        self.assertEqual(data.href, self.glo30_path)
        self.assertEqual(data.title, "N53_00_W115_00")
        self.assertIsNone(data.description)
        self.assertEqual(data.media_type, MediaType.COG)
        self.assertEqual(data.roles, ["data"])

        self.assertTrue(ProjectionExtension.has_extension(item))
        self.assertTrue(RasterExtension.has_extension(item))

        item.validate()  # raises STACValidationError if not

    def test_create_glo90_item(self):
        item = stac.create_item(self.glo90_path)
        self.assertEqual(item.id, "Copernicus_DSM_COG_30_N53_00_W115_00_DEM")
        self.assertIsNotNone(item.geometry)
        self.assertEqual(
            list(item.bbox),
            [-115.000625, 53.000416666666666, -114.000625, 54.000416666666666])
        self.assertEqual(
            item.datetime,
            datetime.datetime(2021, 4, 22, tzinfo=datetime.timezone.utc))

        common_metadata = item.common_metadata
        self.assertEqual(common_metadata.platform, "tandem-x")
        self.assertEqual(common_metadata.gsd, 90)
        expected_providers = [
            Provider("European Space Agency",
                     roles=[ProviderRole.LICENSOR],
                     url=("https://spacedata.copernicus.eu/documents/20126/0/"
                          "CSCDA_ESA_Mission-specific+Annex.pdf")),
            Provider("Sinergise",
                     roles=[ProviderRole.PRODUCER, ProviderRole.PROCESSOR],
                     url="https://registry.opendata.aws/copernicus-dem/"),
            Provider("OpenTopography",
                     roles=[ProviderRole.HOST],
                     url=("https://portal.opentopography.org/"
                          "datasetMetadata?otCollectionID=OT.032021.4326.1"))
        ]
        for expected, actual in zip(expected_providers,
                                    common_metadata.providers):
            self.assertDictEqual(expected.to_dict(), actual.to_dict())
        self.assertEqual(common_metadata.license, "proprietary")

        projection = ProjectionExtension.ext(item)
        self.assertEqual(projection.epsg, 4326)
        self.assertEqual(projection.shape, (1200, 800))
        self.assertEqual(list(projection.transform), [
            0.00125, 0.0, -115.000625, 0.0, -0.0008333333333333334,
            54.000416666666666
        ])

        handbook = item.get_single_link("handbook")
        self.assertIsNotNone(handbook)
        self.assertEqual(handbook.title, "Copernicus DEM User handbook")
        self.assertEqual(handbook.rel, "handbook")
        self.assertEqual(
            handbook.href,
            "https://object.cloud.sdsc.edu/v1/AUTH_opentopography/www/metadata"
            "/Copernicus_metadata.pdf")
        self.assertEqual(handbook.media_type, "application/pdf")

        data = item.assets["data"]
        self.assertEqual(data.href, self.glo90_path)
        self.assertEqual(data.title, "N53_00_W115_00")
        self.assertIsNone(data.description)
        self.assertEqual(data.media_type, MediaType.COG)
        self.assertEqual(data.roles, ["data"])

        self.assertTrue(ProjectionExtension.has_extension(item))
        self.assertTrue(RasterExtension.has_extension(item))

        item.validate()  # raises STACValidationError if not

    def test_create_item_with_read_href_modifier(self):
        done = False

        def do_it(href):
            nonlocal done
            done = True
            return href

        _ = stac.create_item(self.glo30_path, read_href_modifier=do_it)
        self.assertTrue(done, "Didn't do it")

    def test_create_collection(self):
        # Write tests for each for the creation of a STAC Collection
        # Create the STAC Collection...
        collection = stac.create_collection("glo-30")
        collection.set_self_href("")

        # Check that it has some required attributes
        self.assertEqual(collection.id, "cop-dem-glo-30")
        # self.assertEqual(collection.other_attr...

        # Validate
        collection.validate()
