# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

EXAMPLE = [10, 10, 10]


def find_it(seq):
    """returns the int that appears an odd number of times"""
    counter = 0
    seq.sort()
    for i, number in enumerate(seq):
        if len(seq) == 1:
            return seq[0]
        if i != len(seq) - 1:
            num1 = seq[i]
            num2 = seq[i + 1]
            if num1 == num2:
                counter += 1
            elif num1 != num2:
                if counter == 0:
                    return number
                if counter % 2 == 0:
                    return number
                counter = 0
        else:
            if counter == 0:
                return number
            if counter % 2 == 0:
                return number
            break

def find_it2(seq):
    """returns the int that appears an odd number of times"""
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


solution = find_it(EXAMPLE)
print(solution)
