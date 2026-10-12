def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


# Test
assert find_duplicates([10, 20, 30, 20, 40, 10]) == [10, 20]
assert find_duplicates([1, 2, 3, 4]) == []

print("Test Passed: Duplicate Elements")