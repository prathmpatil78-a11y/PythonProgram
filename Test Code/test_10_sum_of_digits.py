def sum_of_digits(number):
    total = 0
    
    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10
        
    return total

#Test
assert sum_of_digits(12345) == 15
assert sum_of_digits(123) == 6

print("Test Passed: Sum of Digits")