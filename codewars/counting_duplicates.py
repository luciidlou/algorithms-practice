# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
EXAMPLE = 'abcdeaa'


def duplicate_count(text):
    """returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string"""
    counter = 0
    formatted_text = text.lower()
    text_list = list(formatted_text)
    text_list.sort()
    for i, _ in enumerate(text_list):
        if i != len(text_list) - 1:
            if text_list[i] != text_list[i - 1]:
                if text_list[i] == text_list[i + 1]:
                    counter += 1
        else:
            break
    return counter

solution = duplicate_count(EXAMPLE)
print(solution)
