import unittest
from lab7 import kruskal
import csv
import os

def create_csv(filename, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

class TestKruskal(unittest.TestCase):

    # звичайний звязний граф
    def test_basic(self):
        create_csv("test1.csv", [
            ["K1", "K2", 2000],
            ["K1", "K3", 3000],
            ["K2", "K3", 1000],
            ["K2", "K4", 4000],
            ["K3", "K4", 2500],
        ])
        result = kruskal("test1.csv")
        self.assertEqual(result, 5500)  

    # незвязний граф 
    def test_disconnected(self):
        create_csv("test2.csv", [
            ["K1", "K2", 1000],
            ["K3", "K4", 2000],
        ])
        result = kruskal("test2.csv")
        self.assertEqual(result, -1)

    # всі ребра однакові
    def test_equal_weights(self):
        create_csv("test5.csv", [
            ["K1", "K2", 100],
            ["K2", "K3", 100],
            ["K3", "K4", 100],
            ["K1", "K4", 100],
        ])
        result = kruskal("test5.csv")
        self.assertEqual(result, 300)  

    # лінійний граф 
    def test_linear(self):
        create_csv("test6.csv", [
            ["K1", "K2", 100],
            ["K2", "K3", 200],
            ["K3", "K4", 300],
            ["K4", "K5", 400],
        ])
        result = kruskal("test6.csv")
        self.assertEqual(result, 1000)

    def tearDown(self):
        for i in range(1, 8):
            filename = f"test{i}.csv"
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == "__main__":
    unittest.main()