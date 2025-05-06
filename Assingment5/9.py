def remove_nth_char(s, n):
    if n < 0 or n >= len(s):
        return "Index out of range"  
    return s[:n] + s[n+1:]


print(remove_nth_char('hello', 2))  
print(remove_nth_char('python', 0))  
print(remove_nth_char('programming', 5)) 