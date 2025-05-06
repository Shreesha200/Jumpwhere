def find_numbers():
    result = []
    for num in range(1500, 2701):  
        if num % 7 == 0 and num % 5 == 0:
            result.append(num)
    return result

numbers = find_numbers()
print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700:")
print(numbers)