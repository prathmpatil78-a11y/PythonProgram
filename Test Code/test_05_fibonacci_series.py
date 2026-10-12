def fibonacci(n):
    series = []
    a = 0
    b = 1
    
    for i in range(n):
        series.append(a)
        a,b = b, a + b
        
    return series

#Test
assert fibonacci(5) ==[0, 1, 1, 2, 3]
assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

print("Test Passed: fibonacci Series")