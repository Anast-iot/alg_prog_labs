import unittest

from lab3 import BinaryTree
self.assertTrue(root.tree_balanced())

class TestIsTreeBalanced(unittest.TestCase):

    def test_balanced_tree_from_task(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        self.assertTrue(tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.right = BinaryTree(3)
        root.left.right.right = BinaryTree(4)

        self.assertFalse(tree_balanced(root))

    def test_single_node(self):
        root = BinaryTree(42)

        self.assertTrue(tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(True) 

if __name__ == "__main__":
    unittest.main()



