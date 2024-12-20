import unittest

from algorithms.greedy.ClassPhotos import ClassPhotos


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cp = ClassPhotos()

    def test_class_photos_true(self):
        red = [5, 8, 1, 2, 4]
        blue = [6, 9, 2, 4, 5]
        result = self.cp.class_photos(red, blue)
        self.assertTrue(result)

    def test_class_photos_false(self):
        red = [5, 8, 1, 2, 4]
        blue = [9, 5, 2, 4, 5]
        result = self.cp.class_photos(red, blue)
        self.assertFalse(result)
