def word_frequency(sentence):
    frequency = {}

    words = sentence.split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# Test
assert word_frequency("python is easy python") == {
    "python": 2,
    "is": 1,
    "easy": 1
}

print("Test Passed: Word Frequency")