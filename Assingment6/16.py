my_list = []
n = int(input("Enter the number of elements you want to add to the list: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

# Take input to search and delete element
search_item = input("Enter the item you want to search and delete: ")

if search_item in my_list:
    my_list.remove(search_item)
    print(f"'{search_item}' has been deleted from the list.")
else:
    print(f"'{search_item}' not found in the list.")

# Iterate over the list and print each element
print("Updated list:")
for item in my_list:
    print(item)
