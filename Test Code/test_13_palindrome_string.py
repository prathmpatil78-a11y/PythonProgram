def check_palindrome(text):
    reverse = ""
    
    for char in text:
        reverse = char + reverse
        
    if text == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
#Test 
assert check_palindrome("madam") == "Palindrome"
assert check_palindrome("hello") == "Not Palindrome"
assert check_palindrome("level") == "Palindrome"

print("Test Passed: Palindrome String")