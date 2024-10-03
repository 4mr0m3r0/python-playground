
# AlgoExpert
class MinimumWaitingTime:

    # Time O(n log n) | Space O(1)
    def minimum_waiting_time(self, queries: list):
        queries.sort()
        total = 0
        for idx, duration in enumerate(queries):
            queries_left = len(queries) - (idx + 1)
            total += duration * queries_left
        return total