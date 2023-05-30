def dna_complement(dna):
    complement = ''
    for letter in dna:
        if letter == 'A':
            complement += 'T'
        elif letter == 'T':
            complement += 'A'
        elif letter == 'C':
            complement += 'G'
        elif letter == 'G':
            complement += 'C'
    return complement