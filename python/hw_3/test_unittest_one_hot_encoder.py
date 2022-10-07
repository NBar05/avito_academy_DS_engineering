from one_hot_encoder import fit_transform
import unittest


class TestOHE(unittest.TestCase):
    def test_len(self):
        self.assertEqual(len(fit_transform(['', 2, '1', 1, ('12', '341')])), 5)

    def test_one_cat(self):
        self.assertTrue(all([el[1][0] == 1 for el in fit_transform(['', '', '', ''])]))

    def test_equal(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertListEqual(fit_transform(cities), expected)

    def test_raise(self):
        with self.assertRaises(TypeError) as cm:
            _ = fit_transform()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'expected at least 1 arguments, got 0')
