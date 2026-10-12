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
    
number = 121

result = check_palindrome(number)
print(result)