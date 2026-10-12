def remove_duplicates(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique


# Test
assert remove_duplicates([10, 20, 10, 30, 20]) == [10, 20, 30]
assert remove_duplicates([1, 1, 2, 2, 3]) == [1, 2, 3]

print("Test Passed: Remove Duplicates")