class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class EvaluateExpressionTree:
    # Big O Notation
    # Time O(n) | Space O(h)
    def evaluate_expression_tree(self, tree: BinaryTree) -> int:
        if tree and tree.value > 0:
            return tree.value
        if tree.value == -1:
            return self.evaluate_expression_tree(tree.left) + self.evaluate_expression_tree(tree.right)
        if tree.value == -2:
            return self.evaluate_expression_tree(tree.left) - self.evaluate_expression_tree(tree.right)
        if tree.value == -3:
            return int(self.evaluate_expression_tree(tree.left) / self.evaluate_expression_tree(tree.right))
        if tree.value == -4:
            return self.evaluate_expression_tree(tree.left) * self.evaluate_expression_tree(tree.right)
        return 0
