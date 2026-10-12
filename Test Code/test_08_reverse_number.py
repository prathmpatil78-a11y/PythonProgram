def reverse_number(number):
    reverse = 0
    
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
        
    return reverse

#Test
assert reverse_number(12345) == 54321
assert reverse_number(123) == 321

print("Test Passed: Reverse a Number")