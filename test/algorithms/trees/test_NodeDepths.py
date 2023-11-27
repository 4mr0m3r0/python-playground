from unittest import TestCase
from algorithms.trees.NodeDepths import NodeDepths
from algorithms.trees.NodeDepths import BinaryTree


class TestNodeDepths(TestCase):
    def setUp(self):
        self.node_depths = NodeDepths()

    def test_given_tree_A_when_node_depths_then_16(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(
                    value=4,
                    left=BinaryTree(value=8),
                    right=BinaryTree(value=9),
                ),
                right=BinaryTree(value=5)
            ),
            right=BinaryTree(
                value=3,
                left=BinaryTree(value=6),
                right=BinaryTree(value=7),
            )
        )
        result = self.node_depths.node_depths(binary_tree)
        self.assertEqual(16, result)

    def test_given_tree_A_when_node_depths_then_4(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(value=4),
            ),
            right=BinaryTree(value=3)
        )
        result = self.node_depths.node_depths(binary_tree)
        self.assertEqual(4, result)

    def test_given_tree_A_when_node_depths_then_21(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(
                    value=3,
                    left=BinaryTree(
                        value=4,
                        left=BinaryTree(
                            value=5,
                            left=BinaryTree(
                                value=6,
                                right=BinaryTree(value=7)
                            )
                        )
                    )
                ),
            ),
        )
        result = self.node_depths.node_depths(binary_tree)
        self.assertEqual(21, result)

    def test_given_tree_A_when_node_depths_iterative_then_16(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(
                    value=4,
                    left=BinaryTree(value=8),
                    right=BinaryTree(value=9),
                ),
                right=BinaryTree(value=5)
            ),
            right=BinaryTree(
                value=3,
                left=BinaryTree(value=6),
                right=BinaryTree(value=7),
            )
        )
        result = self.node_depths.node_depths_iterative(binary_tree)
        self.assertEqual(16, result)

    def test_given_tree_A_when_node_depths_iterative_then_4(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(value=4),
            ),
            right=BinaryTree(value=3)
        )
        result = self.node_depths.node_depths_iterative(binary_tree)
        self.assertEqual(4, result)

    def test_given_tree_A_when_node_depths_iterative_then_21(self):
        binary_tree = BinaryTree(
            value=1,
            left=BinaryTree(
                value=2,
                left=BinaryTree(
                    value=3,
                    left=BinaryTree(
                        value=4,
                        left=BinaryTree(
                            value=5,
                            left=BinaryTree(
                                value=6,
                                right=BinaryTree(value=7)
                            )
                        )
                    )
                ),
            ),
        )
        result = self.node_depths.node_depths_iterative(binary_tree)
        self.assertEqual(21, result)

