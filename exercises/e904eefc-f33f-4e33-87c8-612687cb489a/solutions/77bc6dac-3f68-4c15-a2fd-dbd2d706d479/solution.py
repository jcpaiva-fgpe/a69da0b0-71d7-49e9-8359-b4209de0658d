def word_encryption(sentence):
    words = sentence.split()
    encrypted_words = []
    for word in words:
        encrypted_word = word[::-1]
        encrypted_words.append(encrypted_word)
    return ' '.join(encrypted_words)