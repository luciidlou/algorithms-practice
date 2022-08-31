# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

def get_sum(a, b):
    """finds the sum of all the integers between and including them and returns it. If the two numbers are equal, returns a or b"""
    counter = 0
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        x = range(a, b)
        for n in x:
            counter += n
    return counter

SOLUTION = get_sum(30, 12)
print(SOLUTION)
