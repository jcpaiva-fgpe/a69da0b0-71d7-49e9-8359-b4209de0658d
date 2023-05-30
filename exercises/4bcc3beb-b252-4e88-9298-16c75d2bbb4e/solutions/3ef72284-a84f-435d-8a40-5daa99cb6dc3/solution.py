def highest_scoring_word(words):
    highest_score = 0
    highest_word = ""
    for word in words.split():
        score = sum([ord(c) - 96 for c in word])
        if score > highest_score:
            highest_score = score
            highest_word = word
    return highest_word