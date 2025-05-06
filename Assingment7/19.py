sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_lists = []
for sublist in sample_list:
    if sublist not in unique_lists:
        unique_lists.append(sublist)

print("New List:", unique_lists)