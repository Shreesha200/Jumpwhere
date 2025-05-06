numbers = []
product = 1

while True:
    user_input = input("Enter an integer (press 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    else:
        try:
            num = int(user_input)
            numbers.append(num)
            product *= num
        except ValueError:
            print("Please enter a valid integer.")

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average of all numbers:", average)
    print("Product of all numbers:", product)
else:
    print("No numbers were entered.")