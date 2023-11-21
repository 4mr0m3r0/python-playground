import unittest

from algorithms.trees.BranchSums import BinaryTree
from algorithms.trees.BranchSums import BranchSums


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.branch_sums = BranchSums()

    def test_given_tree_A_when_branch_sums_then_expected_list(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(
                    value=4,
                    left=BinaryTree(value=8),
                    right=BinaryTree(value=9)
                ),
                right=BinaryTree(
                    value=5,
                    left=BinaryTree(value=10)
                )
            ),
            right=BinaryTree(
                value=3,
                left=BinaryTree(value=6),
                right=BinaryTree(value=7),
            )
        )
        result = self.branch_sums.branch_sums(binary_tree)
        self.assertEqual([15, 16, 18, 10, 11], result)

    def test_given_tree_B_when_branch_sums_then_expected_list(self):
        binary_tree = BinaryTree(
            value=0,
            left=BinaryTree(value=9),
            right=BinaryTree(
                value=1,
                left=BinaryTree(value=15),
                right=BinaryTree(
                    value=10,
                    left=BinaryTree(value=100),
                    right=BinaryTree(value=200)
                )
            )
        )
        result = self.branch_sums.branch_sums(binary_tree)
        self.assertEqual([9, 16, 111, 211], result)


if __name__ == '__main__':
    unittest.main()
