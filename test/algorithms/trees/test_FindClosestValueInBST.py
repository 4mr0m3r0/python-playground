import unittest
from algorithms.trees.FindClosestValueInBST import FindClosestValueInBST
from algorithms.trees.FindClosestValueInBST import BST


class TestFindClosestValueInBST(unittest.TestCase):
    def setUp(self):
        self.closest_value_in_bst = FindClosestValueInBST()

    def test_target_12_when_find_closest_value_in_bst_then_return_13(self):
        tree = BST(
            value=10,
            left=BST(
                value=5,
                left=BST(
                    value=2,
                    left=BST(value=1)
                ),
                right=BST(value=5)
            ),
            right=BST(
                value=15,
                left=BST(
                    value=13,
                    right=BST(value=14)
                ),
                right=BST(value=22)
            )
        )
        result = self.closest_value_in_bst.find_closest_value_in_bst(tree=tree, target=12)
        self.assertEqual(13, result)

    def test_target_12_when_find_closest_value_in_bst_iterative_then_return_11(self):
        tree = BST(
            value=9,
            left=BST(
                value=5,
                left=BST(
                    value=2,
                    left=BST(value=1),
                    right=BST(value=3)
                ),
                right=BST(value=8)
            ),
            right=BST(
                value=20,
                left=BST(
                    value=11,
                    left=BST(value=10),
                    right=BST(
                        value=16,
                        left=BST(value=14),
                        right=BST(value=17)
                    )
                ),
                right=BST(value=30)
            )
        )
        result = self.closest_value_in_bst.find_closest_value_in_bst_iterative(tree=tree, target=12)
        self.assertEqual(11, result)

    def test_target_minus_1_when_find_closest_value_in_bst_variant_then_return_1(self):
        tree = BST(
            value=100,
            left=BST(
                # region tree 5
                value=5,
                left=BST(
                    # region tree 2
                    value=2,
                    left=BST(
                        # region tree 1
                        value=1,
                        left=BST(
                            value=-51,
                            left=BST(value=-403)
                        ),
                        right=BST(
                            value=1,
                            right=BST(
                                value=1,
                                right=BST(
                                    value=1,
                                    right=BST(value=1)
                                )
                            )
                        )
                        #endregion
                    ),
                    right=BST(value=3)
                    # endregion
                ),
                right=BST(
                    # region tree 15
                    value=15,
                    left=BST(value=5),
                    right=BST(
                        value=22,
                        right=BST(
                            value=57,
                            right=BST(value=60)
                        )
                    )
                    # endregion
                )
                # endregion
            ),
            right=BST(
                # region tree 502
                value=502,
                left=BST(
                    # region tree 204
                    value=204,
                    left=BST(value=203),
                    right=BST(
                        value=205,
                        right=BST(
                            value=207,
                            left=BST(value=206),
                            right=BST(value=208)
                        )
                    )
                    # endregion
                ),
                right=BST(
                    # region tree 5500
                    value=5500,
                    left=BST(
                        value=1001,
                        right=BST(value=4500)
                    )
                    # endregion
                )
                # endregion
            )
        )
        result = self.closest_value_in_bst.find_closest_value_in_bst_variant(tree=tree, target=-1)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
