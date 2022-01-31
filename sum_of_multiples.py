# pylint: disable=missing-module-docstring, disable=line-too-long, consider-using-enumerate, missing-function-docstring

"""
Sum of Multiples:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

! Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(limit):
    nums = []
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    return sum(nums)


answer = sum_of_multiples(1001)
print(answer)
