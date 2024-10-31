def strings_to_lengths(strings):
    result = {}
    for string in strings:
        result[string] = len(string)
    return result

strings = ["apple", "banana", "cherry"]
print(strings_to_lengths(strings))
