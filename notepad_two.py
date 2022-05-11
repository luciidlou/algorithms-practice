def find_unique_numbers(numbers):
    """bleh"""
    unique_nums = []
    for i in range(len(numbers)):
        if numbers[i] == numbers[i + 1]:
            unique_nums.append(numbers[i])
        else:
            continue
    return unique_nums

if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))