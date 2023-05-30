def is_palindrome(string):
    string = ''.join(e for e in string if e.isalnum()).lower()
    return string == string[::-1]