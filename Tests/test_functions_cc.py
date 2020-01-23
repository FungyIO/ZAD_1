import unittest
import functions_cc


class Test_function_cc(unittest.TestCase):
    def test_cc(self):
        a = dict(functions_cc.get_all_functions_cc('.'))
        print(a)
        self.assertEqual(a['funkcja1'], 'A')
        self.assertEqual(a['funkcja2'], 'A')
        self.assertEqual(a['funkcja3'], 'A')
        self.assertEqual(a['funkcja4'], 'A')