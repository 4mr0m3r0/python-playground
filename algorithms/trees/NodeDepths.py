class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class NodeDepths:
    # Big O Notation
    # Time O(n) | Space O(h)
    def node_depths(self, root: BinaryTree) -> int:
        return self.calculate_sum_nodes(root, 0)

    def calculate_sum_nodes(self, tree: BinaryTree, depth: int) -> int:
        if tree is None:
            return depth
        new_depth = depth
        if tree.left is not None:
            new_depth += self.calculate_sum_nodes(tree.left, depth + 1)
        if tree.right is not None:
            new_depth += self.calculate_sum_nodes(tree.right, depth + 1)
        return new_depth

    def node_depths_iterative(self, root: BinaryTree) -> int:
        total_depth = 0
        stack = [{'node': root, 'depth': 0}]
        while len(stack) > 0:
            node_depth = stack.pop()
            node, depth = node_depth['node'], node_depth['depth']
            if node is None:
                continue
            total_depth += depth
            stack.append({'node': node.left, 'depth': depth + 1})
            stack.append({'node': node.right, 'depth': depth + 1})
        return total_depth
