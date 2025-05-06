mixed = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sorted_mixed = sorted(mixed, key=lambda x: (isinstance(x, str), x))
print(sorted_mixed)
