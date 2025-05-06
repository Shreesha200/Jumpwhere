x = int(input("Input length of side x: "))
y = int(input("Input length of side y: "))
z = int(input("Input length of side z: "))

if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or x == z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")