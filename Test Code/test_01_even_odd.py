def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Test
assert check_even_odd(10) == "Even"
assert check_even_odd(7) == "Odd"

print("Test Passed: Even or Odd")