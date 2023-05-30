def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len).strip(".,!?;:")