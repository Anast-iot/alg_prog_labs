import unittest
from lab8 import find_max_wire_length


class TestWireLength(unittest.TestCase):

    # --- Тести з умови задачі ---

    def test_example_1_alternating_heights(self):
        """Приклад 1: 3 стовпи з max висотою 3, відстань 2.
        Оптимальні висоти: 3, 1, 3 → sqrt(4+4) + sqrt(4+4) = 2*sqrt(8) ≈ 5.66
        Примітка: в умові вказано 5.65, але точний результат 5.657 округлюється до 5.66.
        """
        import math
        w = 2
        heights = [3, 3, 3]
        result = find_max_wire_length(w, heights)
        expected = 2 * math.sqrt(8)   # ≈ 5.6568...
        self.assertAlmostEqual(result, expected, places=2)

    def test_example_2_all_same_height(self):
        """Приклад 2: 4 стовпи однакової висоти 1, відстань 100. Дріт горизонтальний = 300"""
        w = 100
        heights = [1, 1, 1, 1]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 300.0, places=2)

    def test_example_3_alternating_high_low(self):
        """Приклад 3: 5 стовпів, чергування 100/2/100/2/100, відстань 4. Очікується 396.32"""
        w = 4
        heights = [100, 2, 100, 2, 100]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 396.32, places=2)

    def test_example_4_large_input(self):
        """Приклад 4: 50 стовпів, відстань 4. Очікується 2738.18"""
        w = 4
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54,
                   44, 26, 86, 79, 4, 15, 5, 91, 25, 17,
                   88, 66, 28, 2, 95, 97, 60, 93, 40, 70,
                   75, 48, 38, 51, 34, 52, 87, 8, 62, 77,
                   35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 2738.18, places=2)

    # --- Додаткові тести з граничними випадками ---

    def test_two_poles_max_difference(self):
        """Лише 2 стовпи: один може бути висотою 100, інший 1. Відстань 1."""
        w = 1
        heights = [100, 100]
        # Найгірше: один 100, другий 1 → sqrt(1 + 99²) = sqrt(1 + 9801) = sqrt(9802)
        import math
        expected = math.sqrt(1 + 99 * 99)
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, expected, places=2)

    def test_single_pole_no_wire(self):
        """Лише 1 стовп — дріт не потрібен, довжина = 0."""
        w = 10
        heights = [50]
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_all_poles_height_1(self):
        """Всі стовпи мають max висоту 1 — дріт завжди горизонтальний."""
        w = 5
        heights = [1, 1, 1, 1, 1]
        # Всі висоти = 1, дріт горизонтальний: 4 * 5 = 20
        result = find_max_wire_length(w, heights)
        self.assertAlmostEqual(result, 20.0, places=2)


if __name__ == "__main__":
    unittest.main()