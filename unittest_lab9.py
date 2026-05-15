import unittest
from lab9 import kmp_search, build_lps

class TestKmpSearch(unittest.TestCase):

    def test_two_occurrences(self):
        self.assertEqual(
            kmp_search("hello world, hello Python", "hello"), [0, 13]
        )

    def test_classic_kmp_example(self):
        self.assertEqual(
            kmp_search("AABAACAADAABAABA", "AABA"), [0, 9, 12]
        )

    def test_not_found(self):
        self.assertEqual(kmp_search("abcdef", "xyz"), [])

    def test_single_char_needle(self):
        self.assertEqual(kmp_search("banana", "a"), [1, 3, 5])

if __name__ == "__main__":
    unittest.main(verbosity=2)

    