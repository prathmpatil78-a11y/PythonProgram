def find_largest(a, b, c):
    if a >= b and a>= c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c
    
#Test 

assert find_largest(25, 40, 15) == 40
assert find_largest(100, 50, 75) == 100

print("Test Passed: Largest of Three Numbers")