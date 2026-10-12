def remove_duplicates(numbers):
    unique = []
    
    for number in numbers:
        if number not in unique:
            unique.append(number)
            
            
    return unique

numbers = [10, 20, 30, 10, 40, 30]

result = remove_duplicates(numbers)
print("List after removing duplicates:", result)