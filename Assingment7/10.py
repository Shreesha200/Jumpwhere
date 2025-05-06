my_dict = {'a': 100, 'b': 200, 'c': 300}


key_to_remove = 'a'


if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed from the dictionary.")
else:
    print(f"Key '{key_to_remove}' not found.")


print("Updated Dictionary:", my_dict)