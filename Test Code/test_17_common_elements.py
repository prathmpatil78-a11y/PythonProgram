def find_common(list1, list2):
    common = []

    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common


# Test
assert find_common([10, 20, 30, 40], [30, 40, 50]) == [30, 40]
assert find_common([1, 2, 3], [3, 4, 5]) == [3]

print("Test Passed: Common Elements")