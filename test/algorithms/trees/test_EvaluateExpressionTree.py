from unittest import TestCase
from algorithms.trees.EvaluateExpressionTree import BinaryTree
from algorithms.trees.EvaluateExpressionTree import EvaluateExpressionTree


class TestEvaluateExpressionTree(TestCase):
    def setUp(self):
        self.evaluate_expression_tree = EvaluateExpressionTree()

    def test_given_tree_when_evaluate_then_return_6(self):
        binary_tree = BinaryTree(
            value=-1,
            left=BinaryTree(
                value=-2,
                left=BinaryTree(
                    value=-4,
                    left=BinaryTree(value=2),
                    right=BinaryTree(value=3),
                ),
                right=BinaryTree(value=2)
            ),
            right=BinaryTree(
                value=-3,
                left=BinaryTree(value=8),
                right=BinaryTree(value=3),
            )
        )
        actual = self.evaluate_expression_tree.evaluate_expression_tree(binary_tree)
        self.assertEqual(6, actual)
