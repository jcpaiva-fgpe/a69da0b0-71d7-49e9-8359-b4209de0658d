def matching_brackets(s):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in brackets_map:
            if not stack or stack[-1] != brackets_map[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack
