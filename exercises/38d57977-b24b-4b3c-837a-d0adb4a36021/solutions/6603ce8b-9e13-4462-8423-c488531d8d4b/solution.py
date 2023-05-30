def is_pangram(string):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(string.lower())