my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}


top_3 = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3]


print("Highest 3 values in the dictionary:")
for key, value in top_3:
    print(f"{key}: {value}")