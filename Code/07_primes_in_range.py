def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, number):
        if number % i ==0:
            return False
        
    return True


def print_primes(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")
            
start = 1
end = 20

print("Prime numbers:")
print_primes(start, end)