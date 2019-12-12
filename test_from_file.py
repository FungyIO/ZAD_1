import unittest
import podpucha_plik
import parse_functions_names


class TestFile(unittest.TestCase):
    def setUp(self):
        self.podpucha_plik


class TestFrom_file(TestFile):
    def test_parse_functions_names_from_file(self):
        self.assertEqual(parse_functions_names.from_file(parse_functions_names(self.TestFile.setUp())), "['funkcja1', 'funkcja2', 'funkcja3', 'funkcja4']" )
