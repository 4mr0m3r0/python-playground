
# AlgoExpert
class TandemBicycle:

    # Time O(nlog(n)) | Space O(1)
    @staticmethod
    def tandem_bicycle(red_shirt_speeds: list, blue_shirt_speeds: list, fastest: bool) -> int:
        if fastest:
            red_shirt_speeds.sort(reverse=True)
        else:
            red_shirt_speeds.sort()
        blue_shirt_speeds.sort()
        total_speed = 0
        for idx in range(len(red_shirt_speeds)):
            total_speed += max(red_shirt_speeds[idx], blue_shirt_speeds[idx])
        return total_speed