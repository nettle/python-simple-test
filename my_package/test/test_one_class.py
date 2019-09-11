"""
Test cases for one_class module

Module utils implements TestCase helper class
which loads module from upper directory
"""
import unittest

import utils


class TestOneClass(utils.TestCase):
    """Unittest class for one_class module"""
    module_file_name = "one_class.py"

    def test_one_class(self):
        """Test one_class"""
        self.assertTrue(self.module_under_test.One.something)


if __name__ == "__main__":
    unittest.main()
