def reverse_number(number):
    reverse = 0
    
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
        
    return reverse

number = 12345

result = reverse_number(number)
print("Reversed number:", result)