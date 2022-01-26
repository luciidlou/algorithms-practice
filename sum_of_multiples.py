# pylint: disable=missing-module-docstring
def sum_of_multiples(limit):
    """Sums all the numbers divisible by 3 or 5 that are within 0-limit.

    Args:
        limit (int): the number you want to stop the iteration at.

    Returns:
        int: a sum of numbers.
    """
    nums = []
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    return sum(nums)


answer = sum_of_multiples(1001)
print(answer)
