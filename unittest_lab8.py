import unittest
from lab8 import find_max_wire_length

class TestWireLength(unittest.TestCase):

    def test_example_1_alternating_heights(self):
        import math
        w = 2
        heights = [3, 3, 3]
        result = find_max_wire_length(w, heights)
        expected = 2 * math.sqrt(8)   
        self.assertAlmostEqual(result, expected, places=2)

    def test_example_2_all_same_height(self):
        w = 100
        heights = [1, 1, 1, 1]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 300.0, places=2)

    def test_example_3_alternating_high_low(self):
        w = 4
        heights = [100, 2, 100, 2, 100]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 396.32, places=2)

    def test_example_4_large_input(self):
        w = 4
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54,
                   44, 26, 86, 79, 4, 15, 5, 91, 25, 17,
                   88, 66, 28, 2, 95, 97, 60, 93, 40, 70,
                   75, 48, 38, 51, 34, 52, 87, 8, 62, 77,
                   35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 2738.18, places=2)

    def test_single_pole_no_wire(self):
        w = 10
        heights = [50]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_all_poles_height_1(self):
        w = 5
        heights = [1, 1, 1, 1, 1]
        # Всі висоти = 1, дріт горизонтальний: 4 * 5 = 20
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 20.0, places=2)


if __name__ == "__main__":
    unittest.main()
