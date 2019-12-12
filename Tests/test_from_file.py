import unittest
import parse_functions_names


class TestFrom_file(unittest.TestCase):
    def test_parse_functions_names_from_file(self):
        list_of_functions = parse_functions_names.from_file('test_file.py')
        self.assertEqual(list_of_functions, ['funkcja1', 'funkcja2', 'funkcja3', 'funkcja4'])
