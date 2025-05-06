def longest_word_length(words):
   
    longest = max(words, key=len)
    return len(longest)


words_list = ['apple', 'banana', 'cherry', 'date']
print(longest_word_length(words_list))  