
#
# AlgoExpert
#
class ClassPhotos:

    # Time O(n log n) | Space O(1)
    def class_photos(self, red_shirt_heights: list, blue_shirt_heights: list) -> bool:
        red_shirt_heights.sort(reverse=True)
        blue_shirt_heights.sort(reverse=True)
        shirt_color_in_first_row = 'RED' if red_shirt_heights[0] < blue_shirt_heights[0] else 'BLUE'
        for idx in range(len(red_shirt_heights)):
            red_shirt_height = red_shirt_heights[idx]
            blue_shirt_height = blue_shirt_heights[idx]
            if shirt_color_in_first_row == 'RED':
                if red_shirt_height >= blue_shirt_height:
                    return False
            else:
                if blue_shirt_height >= red_shirt_height:
                    return False
        return True