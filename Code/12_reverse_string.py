def reverse_string(text):
    reverse = ""
    
    for char in text:
        reverse = char + reverse
        
    return reverse 

text = "Hello"

result = reverse_string(text)
print("Reversed string:", result)