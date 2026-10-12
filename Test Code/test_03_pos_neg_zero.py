def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
#Test

assert check_number(10) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(0) == "Zero"

print("Test Passed: Positive, Negative, or Zero")