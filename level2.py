import unittest

def is_monotonic(arr):
    if len(arr) <= 2:
        return True
    
    increasing = True
    decreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False

        if arr[i] > arr[i - 1]:
            decreasing = False

    return increasing or decreasing

class TestMonotonic(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(is_monotonic([4, 5, 6, 7, 8, 9]))

    def test_decreasing(self):
        self.assertTrue(is_monotonic([9, 8, 7, 6, 5, 4]))

    def test_not_monotonic(self):
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4]))
        

if __name__ == "__main__":
    unittest.main()