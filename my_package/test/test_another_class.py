"""
Test cases for one_class module

Module utils implements load_upper_module function
which loads module from upper directory
"""
import unittest

import utils


class TestOneClassAlternative(unittest.TestCase):
    """Unittest class for one_class module"""

    @classmethod
    def setUpClass(cls):
        """Load module"""
        cls.module_under_test = utils.load_upper_module("one_class.py")

    def test_one_class(self):
        """Test one_class"""
        self.assertTrue(self.module_under_test.One.something)


if __name__ == "__main__":
    unittest.main()
