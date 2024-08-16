from typing import List

class DepthFirstSearch:
    def __init__(self, name):
        self.children: List[DepthFirstSearch] = []
        self.name = name

    def add_child(self, name):
        self.children.append(DepthFirstSearch(name))

    # Time O(v + e) | Space O(v)
    def depth_first_search(self, array: list):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
