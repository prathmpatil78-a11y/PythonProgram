def reverse_string(text):
    reverse = ""
    
    for char in text:
        reverse = char + reverse
        
    return reverse

#Test
assert reverse_string("Hello") == "olleH"
assert reverse_string("Python") == "nohtyP"

print("Test Passed: Reverse String")