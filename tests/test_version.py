import unittest

import superconfig


class VersionTestCase(unittest.TestCase):
    """Version tests"""

    def test_version(self):
        """check superconfig exposes a version attribute"""
        self.assertTrue(hasattr(superconfig, "__version__"))
        self.assertIsInstance(superconfig.__version__, str)


if __name__ == "__main__":
    unittest.main()
