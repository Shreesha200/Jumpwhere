my_dict = {'a': 2, 'b': 3, 'c': 4}


result = 1
for value in my_dict.values():
    result *= value


print("Product of all values in the dictionary:", result)