def rot13(text):
    ciphered_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                ciphered_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                ciphered_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            ciphered_text += char
    return ciphered_text