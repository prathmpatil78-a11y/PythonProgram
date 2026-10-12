def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = 10

result = check_even_odd(number)
print(result)