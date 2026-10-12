def find_missing(numbers):
    n = len(numbers) + 1
    
    total = n * (n + 1) // 2
    
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
        
    return total - sum_numbers

numbers = [1, 2, 3, 5, 6]

result = find_missing(numbers)
print("Missing number:", result)