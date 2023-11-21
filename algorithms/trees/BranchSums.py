class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BranchSums:
    # Big O Notation
    # Time O(n) | Space O(n)
    def branch_sums(self, root: BinaryTree) -> list:
        return self.add_branch_sums_to_list([], root, 0)

    def add_branch_sums_to_list(self, branches: list, root: BinaryTree, node_sum: int) -> list:
        if root is None:
            return branches
        new_sum = root.value + node_sum
        if root.left is None and root.right is None:
            branches.append(new_sum)
        else:
            if root.left is not None:
                self.add_branch_sums_to_list(branches, root.left, new_sum)
            if root.right is not None:
                self.add_branch_sums_to_list(branches, root.right, new_sum)
        return branches

