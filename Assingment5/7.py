def replace_not_poor(s):
    not_index = s.find('not')
    poor_index = s.find('poor')


    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        
        return s[:not_index] + 'good' + s[poor_index + 4:]
    return s


print(replace_not_poor('The lyrics is not that poor!'))  
print(replace_not_poor('The lyrics is poor!'))     