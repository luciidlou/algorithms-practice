# pylint: disable=missing-module-docstring, disable=line-too-long, consider-using-enumerate, missing-function-docstring

"""
! Your job is to count how many buildings currently are the highest.

Example:
const buildings = [ 1250, 800, 600, 1250, 750 ]
The current maximum height buildings are 1250 meters high.
There are 2 of them, so return 2 from the function.

Function Description:
The function should accept an array of numbers as input.

Returns:
The number of buildings that are tallest.
"""
buildings = [1150, 3023, 2020, 3023, 3023]


def tallest_buildings(arr):
    largest_heights = []
    for num in arr:
        if num == max(arr):
            largest_heights.append(num)

    return len(largest_heights)


ANSWER = tallest_buildings(buildings)
print(ANSWER)
