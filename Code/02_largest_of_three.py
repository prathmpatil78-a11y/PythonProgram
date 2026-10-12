def find_largest(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
a = 25
b = 40
c = 15
largest = find_largest(a, b, c)
print("Largest number:", largest)