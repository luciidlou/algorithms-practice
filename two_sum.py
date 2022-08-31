"""INSERT DOCSTRING HERE"""
from typing import Optional


def two_sum(nums: list[int], target: int) -> Optional[list[int]]:
    """Study this"""
    hashmap: dict = {}
    for i, element in enumerate(nums):
        print(f"loop: {i} ---------------------------------")

        complement = target - element

        print(f"complement: {complement}")

        if complement in hashmap:
            print(f"ANSWER: {[i, hashmap[complement]]}")
            break
        hashmap[element] = i
        print(f"hashmap: {hashmap}")


test_nums: list[int] = [3, 7, 2, 10, 1]
test_target: int = 17

two_sum(nums=test_nums, target=test_target)
