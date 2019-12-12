from unittest import TestCase
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import directory_filenames


class test_get_current_directory_filenames(TestCase):
    def test_get_current_directory_filenames(self):
        list_of_files = directory_filenames.get_current_directory_filenames("/test_folder")
        self.assertEqual(sorted(list_of_files), sorted(['file_1.py', 'file_2.py']))
