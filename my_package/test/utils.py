"""
load_upper_module() function and TestCase class
which load module from directory above
implementing the following directory structure:
  sample.py
  test/test_sample.py
"""
import imp
import os
import unittest


def load_upper_module(file_name):
    """Load module from upper directory (..) by file name"""
    module_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, file_name))
    return imp.load_source(file_name, module_path)


class TestCase(unittest.TestCase):
    """TestCase class which loads module_file_name as a module under test"""

    @classmethod
    def setUpClass(cls):
        """Load module"""
        cls.module_under_test = load_upper_module(cls.module_file_name)
