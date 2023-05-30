def reverse_string_word_by_word(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    output_string = " ".join(reversed_words)
    return output_string