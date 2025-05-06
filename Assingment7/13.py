my_dict = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}

new_dict = {}
for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Dictionary after removing duplicates:")
print(new_dict)