def check_palindrome(number):
    original = number
    reverse = 0
    
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit 
        number = number // 10
        
    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
#Test 
assert check_palindrome(121) == "Palindrome"
assert check_palindrome(123) == "Not Palindrome"
assert check_palindrome(1221) == "Palindrome"

print("Test Passed: Check if a Number is a Palindrome")