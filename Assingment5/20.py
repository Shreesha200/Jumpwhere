def remove_consecutive_duplicates(s):
    result = []
    
    for i in range(len(s)):
        if i == 0 or s[i] != s[i - 1]:
            result.append(s[i])

    return ''.join(result)

sample_string = "aaabbccddaaa"
result = remove_consecutive_duplicates(sample_string)

print(result)