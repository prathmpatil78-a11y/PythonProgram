def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]
    
    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number
    return second 

numbers = [10, 24, 7, 89, 45]

result = second_largest(numbers)
print("Second largest number: ", result)