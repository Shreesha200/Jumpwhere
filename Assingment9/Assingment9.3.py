def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Example usage
input_str = "([{}])"
print(is_balanced(input_str))  # Output: True
print(is_balanced("([)]"))    # False
print(is_balanced("([])"))    # True
print(is_balanced("([]{}))")) # False