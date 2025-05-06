even_numbers = [num for num in range(1, 101) if num % 2 == 0]

odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_numbers = [num for num in range(1, 101) if is_prime(num)]


print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Prime numbers:", prime_numbers)