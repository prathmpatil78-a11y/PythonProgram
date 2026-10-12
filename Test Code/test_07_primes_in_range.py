def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, number):
        if number % i ==0:
            return False
        
    return True

def print_primes(start, end):
    primes = []
    
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
            
    return primes

#Test 
assert print_primes(1, 10) == [2, 3, 5, 7]
assert print_primes(10, 20) == [11, 13, 17, 19]

print("Test Passed: Prime Numbers in Range")