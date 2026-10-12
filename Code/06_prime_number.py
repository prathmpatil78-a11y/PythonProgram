def check_prime(number):
    if number <= 1:
        return "Not Prime"

    for i in range(2, number):
        if number % i == 0:
            return "Not Prime"

    return "Prime"


number = 17

result = check_prime(number)
print(result)