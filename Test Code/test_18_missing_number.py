def find_missing(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    sum_numbers = 0

    for number in numbers:
        sum_numbers += number

    return total - sum_numbers


# Test
assert find_missing([1, 2, 3, 5, 6]) == 4
assert find_missing([1, 2, 3, 4, 6]) == 5

print("Test Passed: Missing Number")