import unittest
from beer import solve, parse_input


def run(raw):
    n, b, matrix = parse_input(raw)
    return solve(matrix, n, b)


class TestBeer(unittest.TestCase):

    def test_example_1(self): # 1 умова
        self.assertEqual(run("2 2\nYN NY"), 2)

    def test_example_2(self): # 2 умова
        self.assertEqual(run("6 3\nYNN YNY YNY NYY NYY NYN"), 2)

    def test_one_beer_everyone_likes(self): # всі люблять одне пиво
        self.assertEqual(run("4 3\nYNN YNY YNN YNN"), 1)

    def test_each_worker_likes_unique_beer(self): # кожен тільки своє любить
        self.assertEqual(run("3 3\nYNN NYN NNY"), 3)

    def test_smaller_set_wins(self):
        self.assertEqual(run("6 3\nYNN YNN YNN NYN NYN NNY"), 3)

    def test_minimum_input(self): # 1 працівник, 1 пиво любить 
        self.assertEqual(run("1 1\nY"), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)