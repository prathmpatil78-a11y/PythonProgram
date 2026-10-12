def check_palindrome(text):
    reverse = ""
    
    for char in text :
        reverse = char + reverse
        
    if text == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
text = "madam"

result = check_palindrome(text)
print(result)