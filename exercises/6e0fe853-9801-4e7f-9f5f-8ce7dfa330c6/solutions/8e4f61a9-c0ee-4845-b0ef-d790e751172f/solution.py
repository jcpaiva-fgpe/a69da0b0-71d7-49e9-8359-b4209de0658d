def is_pangram(string):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(string.lower()))