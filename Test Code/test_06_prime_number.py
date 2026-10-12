def check_prime(number):
    if number <= 1:
        return "Not Prime"
    
    for i in range(2, number):
        if number % i == 0:
            return "Not Prime"
        
    return "Prime"

#Test 
assert check_prime(17) == "Prime"
assert check_prime(10) == "Not Prime"
assert check_prime(2) == "Prime"

print("Test Passed: Prime Number")