import unittest
from BST import BinarySearchTree, InvalidTreeValueError


class TestBinarySearchTree(unittest.TestCase):

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertEqual(bst.value, 10)

    def test_insert_duplicate(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)
        self.assertEqual(bst.value, 10)

    def test_check_if_exists(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertIsNone(bst.check_if_exists(5))

    def test_check_if_exists_not_found(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertIsNone(bst.check_if_exists(5))

    def test_check_if_exists_invalid_type(self):
        bst = BinarySearchTree()
        bst.insert(10)
        with self.assertRaises(InvalidTreeValueError):
            bst.check_if_exists("kot")

    def test_show_in_order(self):
        bst = BinarySearchTree()
        nums = [10, 5, 15, 3, 7, 12, 17]
        for num in nums:
            bst.insert(num)
        expected_result = [3, 5, 7, 10, 12, 15, 17]
        self.assertEqual(bst.show_in_order(), expected_result)


if __name__ == "__main__":
    unittest.main()
