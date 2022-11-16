import unittest

import stactools.cop_dem


class TestModule(unittest.TestCase):

    def test_version(self):
        self.assertIsNotNone(stactools.cop_dem.__version__)
