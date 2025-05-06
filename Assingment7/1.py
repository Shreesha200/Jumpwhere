def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

sample_dict = {
    'pen': 3,
    'notebook': 10,
    'eraser': 1,
    'pencil': 5,
    'hello':6
}

print("Sorted in Ascending Order:")
print(sort_dict_by_value(sample_dict, ascending=True))

print("\nSorted in Descending Order:")
print(sort_dict_by_value(sample_dict, ascending=False))