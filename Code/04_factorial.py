def factorial(number):
    result = 1
    
    for i in range(1, number + 1):
        result = result * i
    return result

number = 5
result = factorial(number)
print("Factorial:", result)