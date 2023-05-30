def balanced_brackets(brackets_string):
    stack = []
    for bracket in brackets_string:
        if bracket in ['(', '[', '{']:
            stack.append(bracket)
        else:
            if not stack:
                return False
            if (bracket == ')' and stack[-1] == '(') or \
               (bracket == ']' and stack[-1] == '[') or \
               (bracket == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                return False
    return not stack