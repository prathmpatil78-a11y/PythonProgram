def count_frequency(text):
    frequency = {}
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency 

text = "hello"

result = count_frequency(text)

for char, count in result.items():
    print(char, ":", count)