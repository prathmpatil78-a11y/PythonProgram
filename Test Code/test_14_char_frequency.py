def count_frequency(text):
    frequency = {}
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

#Test
assert count_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o":1
}

print("Test Passed: character Frequency")