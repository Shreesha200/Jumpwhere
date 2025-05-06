mixed_list = [1, 'apple', 3.14, 5, 'banana', 2.71, 'cherry', 4]

integers = [item for item in mixed_list if isinstance(item, int)]
strings = [item for item in mixed_list if isinstance(item, str)]
floats = [item for item in mixed_list if isinstance(item, float)]