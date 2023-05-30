def most_used_word(sentence):
    sentence_list = sentence.split()
    word_count = {}
    for word in sentence_list:
        if word.lower() in word_count:
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()] = 1
    return max(word_count, key=word_count.get)