# pylint: disable=missing-module-docstring
buildings = [1150, 3023, 2020, 3023, 3023]


def tallest_buildings(arr):  # pylint: disable=missing-function-docstring
    largest_heights = []
    for num in arr:
        if num == max(arr):
            largest_heights.append(num)

    return len(largest_heights)


ANSWER = tallest_buildings(buildings)
print(ANSWER)
