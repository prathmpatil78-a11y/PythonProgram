def second_largest(numbers):
    largets = numbers[0]
    second = numbers[0]
    
    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second

# Test
assert second_largest([10, 25, 7, 89, 45]) == 45
assert second_largest([10, 20, 30, 40]) == 30

print("Test Passed: Second Largest Number")