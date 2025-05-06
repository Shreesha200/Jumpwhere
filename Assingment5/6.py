def add_ing_or_ly(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

print(add_ing_or_ly('abc'))    
print(add_ing_or_ly('string')) 
print(add_ing_or_ly('hi'))