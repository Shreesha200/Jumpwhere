from collections import Counter

d1 = {'a': 100, 'b': 500, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = Counter(d1) + Counter(d2)

print("Combined Dictionary with added values for common keys:")
print(combined_dict)