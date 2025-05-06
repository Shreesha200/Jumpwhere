def unique_sorted_words():
    words = input("Enter a comma-separated sequence of words: ").split(',')
    
    unique_words = sorted(set(word.strip() for word in words))
    
    print(', '.join(unique_words))

unique_sorted_words()