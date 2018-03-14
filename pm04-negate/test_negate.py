import unittest

from negate import negate


class NegateTests(unittest.TestCase):

    """Tests for negate."""

    def test_empty(self):
        self.assertEqual(negate([[]]), [[]])

    def test_single_item(self):
        self.assertEqual(negate([[5]]), [[-5]])

    def test_two_by_two_matrix(self):
        inputs = [[1, 2], [3, 4]]
        outputs = [[-1, -2], [-3, -4]]
        self.assertEqual(negate(inputs), outputs)

    def test_two_by_three_matrix(self):
        inputs = [[1, 2, 3], [4, 5, 6]]
        outputs = [[-1, -2, -3], [-4, -5, -6]]
        self.assertEqual(negate(inputs), outputs)

    def test_three_by_two_matrix(self):
        inputs = [[1, 2], [3, 4], [5, 6]]
        outputs = [[-1, -2], [-3, -4], [-5, -6]]
        self.assertEqual(negate(inputs), outputs)

    def test_three_by_three_matrix(self):
        inputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        outputs = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(negate(inputs), outputs)

    def test_negative_numbers(self):
        inputs = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        outputs = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]
        self.assertEqual(negate(inputs), outputs)


if __name__ == "__main__":
    unittest.main()