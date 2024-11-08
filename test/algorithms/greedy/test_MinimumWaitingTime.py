from unittest import TestCase

from algorithms.greedy.MinimumWaitingTime import MinimumWaitingTime


class TestMinimumWaitingTime(TestCase):
    def setUp(self):
        self.mwt = MinimumWaitingTime()

    def test_minimum_waiting_time(self):
        queries = [3, 2, 1, 2, 6]
        result = self.mwt.minimum_waiting_time(queries)
        self.assertEqual(17, result)
