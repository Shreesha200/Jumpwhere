def first_last_two_chars(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

print(first_last_two_chars('thisisniceone'))  
print(first_last_two_chars('ab'))            
print(first_last_two_chars('f'))      