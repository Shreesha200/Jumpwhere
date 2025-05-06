def find_smallest_largest_word(s):

    words = s.split()
    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    
    return smallest_word, largest_word

sample_string = "The quick brown fox jumped over the lazy dog"
smallest, largest = find_smallest_largest_word(sample_string)

print(f"Smallest word: {smallest}")
print(f"Largest word: {largest}")