import unittest
import math

from linearalgebra import vector as v

class VectorTest(unittest.TestCase):
    """Tests functions in vector.py"""

    def test_magnitude(self):
        """Tests the magnitude() function"""

        vector = v.Vector()
        result = vector.magnitude(1, 1, 1)
        self.assertEqual(result, math.sqrt(3))

    def test_dot_product(self):
        """Tests the dot_product() function"""

        vector = v.Vector()
        result = vector.dot_product(1, 1, 1, 1, 1, 1)
        self.assertEqual(result, 3)

    def test_vector_product(self):
        """Tests the vector_product() function"""

        vector = v.Vector()
        result = vector.vector_product(2, 3, 4, 5, 6, 7)
        self.assertEqual(result, [-3, 6, -3])

    def test_add_vectors(self):
        """Tests the add_vectors() function"""

        vector = v.Vector()
        result = vector.add_vectors(2, 3, 6, 5, 6, 7)
        self.assertEqual(result, [8, 8, 13])

    def test_subtract_vectors(self):
        """Tests the subtract_vectors() function"""

        vector = v.Vector()
        result = vector.subtract_vectors(3, 5, 1, 2, 1, 9)
        self.assertEqual(result, [2, 3, -8])

    def test_multiply_vectors(self):
        """Tests the multiply_vectors() function"""

        vector = v.Vector()
        result = vector.multiply_vectors(2, 3, 4, 5, 6, 7)
        self.assertEqual(result, [8, 15, 42])


if __name__ == '__main__':
    unittest.main()
