class BST:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class FindClosestValueInBST:
    # Big O Notation.
    # Average: Time O(log(n)) | Space O(log(n))
    # Worst: Time O(n) | Space O(n)
    def find_closest_value_in_bst_variant(self, tree, target):
        if tree.value < target:
            if tree.right is None:
                return tree.value
            child_node = self.find_closest_value_in_bst_variant(tree.right, target)
            child_distance = abs(child_node - target)
            self_distance = abs(target - tree.value)
            if child_distance < self_distance:
                return child_node
            else:
                return tree.value
        elif tree.value > target:
            if tree.left is None:
                return tree.value
            child_node = self.find_closest_value_in_bst_variant(tree.left, target)
            child_distance = abs(child_node - target)
            self_distance = abs(target - tree.value)
            if child_distance < self_distance:
                return child_node
            else:
                return tree.value
        else:
            return tree.value

    # Big O Notation.
    # Average: Time O(log(n)) | Space O(log(n))
    # Worst: Time O(n) | Space O(n)
    def find_closest_value_in_bst(self, tree, target):
        return self.recursive_bst(tree, target, float("inf"))

    def recursive_bst(self, tree, target, closest):
        if tree is None:
            return closest
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            return self.recursive_bst(tree.left, target, closest)
        elif target > tree.value:
            return self.recursive_bst(tree.right, target, closest)
        else:
            return closest

    # Big O Notation.
    # Average: Time O(log(n)) | Space O(1)
    # Worst: Time O(n) | Space O(1)
    def find_closest_value_in_bst_iterative(self, tree, target):
        return self.iterative_bst(tree, target, float("inf"))

    def iterative_bst(self, tree, target, closest):
        node = tree
        while node is not None:
            if abs(target - closest) > abs(target - node.value):
                closest = node.value
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                break
        return closest
