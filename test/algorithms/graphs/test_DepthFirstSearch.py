import unittest

from algorithms.graphs.DepthFirstSearch import DepthFirstSearch


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.depth_first_search = DepthFirstSearch(name="A")

    def test_given_graph_then_expected_array(self):
        b = DepthFirstSearch(name="B")
        c = DepthFirstSearch(name="C")
        d = DepthFirstSearch(name="D")
        e = DepthFirstSearch(name="E")
        f = DepthFirstSearch(name="F")
        i = DepthFirstSearch(name="I")
        j = DepthFirstSearch(name="J")
        g = DepthFirstSearch(name="G")
        k = DepthFirstSearch(name="K")
        h = DepthFirstSearch(name="H")
        f.children.extend([i, j])
        b.children.extend([e, f])
        g.children.append(k)
        d.children.extend([g, h])
        self.depth_first_search.children.extend([b, c, d])
        result = self.depth_first_search.depth_first_search(array=[])
        self.assertEqual(
            ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"],
            result
        )


if __name__ == '__main__':
    unittest.main()
