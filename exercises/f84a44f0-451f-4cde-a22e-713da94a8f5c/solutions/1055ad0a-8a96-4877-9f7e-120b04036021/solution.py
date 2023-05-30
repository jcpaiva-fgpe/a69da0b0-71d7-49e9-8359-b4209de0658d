def frequency_counter(text):
    text = text.lower().replace('.','').replace(',','').split()
    freq_dict = {}
    for word in text:
        freq_dict[word] = freq_dict.get(word,0) + 1
    return str(freq_dict)