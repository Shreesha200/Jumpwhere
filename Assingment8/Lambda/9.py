words = ['red', 'black', 'white', 'green', 'orange']
substr1 = 'ack'
substr2 = 'abc'

result1 = list(filter(lambda x: substr1 in x, words))
result2 = list(filter(lambda x: substr2 in x, words))

print(result1)  # ['black']
print(result2)  # []
