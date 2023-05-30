def balanced_parenthesis(string):
    stack = []
    dict = {']':'[', '}':'{', ')':'('}
    for char in string:
        if char in '[{(': # If opening bracket append to stack
            stack.append(char)
        elif char in ']})': # if closing bracket match to opening bracket
            if len(stack) == 0: # if no opening bracket return false, stack cannot be empty if there is a closing bracket in string
                return False
            elif dict[char] == stack[-1]: # if closing bracket matches to opening bracket at the top of stack, pop top of stack
                stack.pop()
            else: # closing bracket does not match opening bracket
                return False
    return len(stack) == 0
