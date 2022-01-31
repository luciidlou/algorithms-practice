# pylint: disable=missing-module-docstring, disable=line-too-long, consider-using-enumerate, missing-function-docstring, invalid-name
"""
Palindrome Numbers:
? A palindromic number reads the same both ways. The largest palindromemade from the product of two 2-digit numbers is 9009 = 91 x 99.

! Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome_numbers(start, stop):
    palindromes_list = []
    for i in range(start, stop):
        for n in range(start, stop):
            product = i * n
            if str(product) == str(product)[::-1]:
                palindromes_list.append(product)
            else:
                continue

    palindromes_list.sort()
    answer = max(palindromes_list)
    return answer


found_palindrome = palindrome_numbers(100, 1000)

print(found_palindrome)
