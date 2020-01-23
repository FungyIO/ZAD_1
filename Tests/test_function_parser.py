from unittest import TestCase
import os
import sys

from parse_functions_names import from_file
from function_parser import parse_function_2
# Allows import files from parent folder
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class test_function_parser(TestCase):
    def test_function_parser(self):
        list_of_functions = from_file('test_file.py')
        list_of_functions += from_file('test_file_2.py')
        tmp_tuple = sorted(parse_function_2('test_file.py', list_of_functions))
        result_tuple = sorted([('funkcja1', 'funkcja2', 1), ('funkcja3', 'funkcja5', 1), ('funkcja4', 'funkcja1', 2)])
        self.assertEqual(sorted(tmp_tuple), result_tuple)

