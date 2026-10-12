def find_duplicates(numbers):
    duplicates = []
    
    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
            
    return duplicates 

numbers = [10, 20, 30, 20, 40, 10, 50]

result = find_duplicates(numbers)
print("Duplicate elements:", result)