total = 0

for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    total += num

average = total / 10
print("The average value is:", average)