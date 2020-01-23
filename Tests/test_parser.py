from unittest import TestCase
import parse_filenames as pf
import directory_filenames


class Test_parse_filenames(TestCase):
    def test_parsefilenames(self):
        a = directory_filenames.get_current_directory_filenames('/Tests')
        list_of_files = pf.parse_function('test_file.py', a, '/Tests')
        self.assertEqual(sorted(list_of_files), sorted([]))