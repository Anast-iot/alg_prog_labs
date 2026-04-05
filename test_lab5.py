import unittest
from lab5 import bfs

class TestKnightBFS(unittest.TestCase):

    # Приклад з умови
    def test_example_from_task(self):
        self.assertEqual(bfs(8, (7, 0), (0, 7)), 6)

    # Дошка 1х1: старт і фініш однаова клітинка
    def test_board_1x1(self):
        self.assertEqual(bfs(1, (0, 0), (0, 0)), 0)

    # Дошка 3х3
    def test_small_board_3x3_center(self):
        self.assertEqual(bfs(3, (0, 0), (2, 2)), 4)

    # Дошка 5х5
    def test_small_board_5x5(self):
        self.assertEqual(bfs(5, (4, 0), (0, 4)), 4)

    # Дошка 10х10
    def test_large_board_corner_to_corner(self):
        result = bfs(10, (0, 0), (9, 9))
        self.assertGreater(result, 0)

    def test_trap_close_positions(self):
        self.assertEqual(bfs(8, (0, 0), (1, 1)), 4)

if __name__ == "__main__":
    unittest.main()