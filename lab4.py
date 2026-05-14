import unittest
from Red_black_priority_queue import RedBlackPriorityQueue


class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.q = RedBlackPriorityQueue()

    def _check_rb(self, q):
        self.assertEqual(q.root.color, False)

        def check(node):
            if node is q.NIL:
                return 1
            if node.color == True:
                self.assertEqual(node.left.color, False)
                self.assertEqual(node.right.color, False)
            left_bh = check(node.left)
            right_bh = check(node.right)
            self.assertEqual(left_bh, right_bh)
            if node.color == False:
                return left_bh + 1
            return left_bh

        check(q.root)

    def _check_order(self, q):
        def check(node):
            if node is q.NIL:
                return
            if node.left is not q.NIL:
                self.assertLessEqual(node.priority, node.left.priority)
            if node.right is not q.NIL:
                self.assertGreater(node.priority, node.right.priority)
            check(node.left)
            check(node.right)
        check(q.root)

    def _size(self, q):
        def count(node):
            if node is q.NIL:
                return 0
            return 1 + count(node.left) + count(node.right)
        return count(q.root)

    def test_enqueue_single(self):
        self.q.enqueue("A", 10)
        val, pri = self.q.peek()
        self.assertEqual(val, "A")
        self.assertEqual(pri, 10)

    def test_enqueue_rb_and_order(self):
        for p in [5, 15, 3, 20, 8]:
            self.q.enqueue("v", p)
        self._check_rb(self.q)
        self._check_order(self.q)

    def test_peek_returns_max(self):
        self.q.enqueue("cat", 8)
        self.q.enqueue("dog", 3)
        self.q.enqueue("bird", 15)
        val, pri = self.q.peek()
        self.assertEqual(pri, 15)
        self.assertEqual(val, "bird")

    def test_peek_does_not_remove(self):
        self.q.enqueue("A", 10)
        self.q.enqueue("B", 20)
        self.q.peek()
        self.q.peek()
        self.assertEqual(self._size(self.q), 2)

    def test_peek_empty_raises(self):
        with self.assertRaises(IndexError):
            self.q.peek()

    def test_dequeue_returns_max(self):
        self.q.enqueue("low", 2)
        self.q.enqueue("mid", 7)
        self.q.enqueue("high", 15)
        val, pri = self.q.dequeue()
        self.assertEqual(pri, 15)
        self.assertEqual(val, "high")

    def test_dequeue_sorted_order(self):
        for p in [5, 12, 3, 18, 7]:
            self.q.enqueue("v", p)
        result = []
        while self.q.root is not self.q.NIL:
            _, pri = self.q.dequeue()
            result.append(pri)
        self.assertEqual(result, [18, 12, 7, 5, 3])

    def test_dequeue_empty_raises(self):
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test_interleaved_operations(self):
        self.q.enqueue("A", 5)
        self.q.enqueue("B", 15)
        self.q.dequeue()
        self.q.enqueue("C", 20)
        self.q.enqueue("D", 8)
        self._check_rb(self.q)
        self._check_order(self.q)
        _, pri = self.q.peek()
        self.assertEqual(pri, 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
