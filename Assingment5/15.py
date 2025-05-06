from collections import Counter

def count_repeated_characters(s):
    char_count = Counter(s)
    

    for char, count in char_count.items():
        if count > 1:
            print(f"{char} {count}")


sample_string = 'thequickbrownfoxjumpsoverthelazydog'
count_repeated_characters(sample_string)