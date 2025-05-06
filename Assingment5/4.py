def change_char(s):
    if not s:
        return ''
    first_char = s[0]
   
    modified_string = first_char + s[1:].replace(first_char, '$')
    return modified_string

print(change_char('restart'))  