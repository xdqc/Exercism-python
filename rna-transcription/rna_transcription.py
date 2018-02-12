def to_rna(dna):
    if list(filter(lambda c: not c in 'ATGC', dna)):
        return ''
    return ''.join(map(base_to_rna, dna))


def base_to_rna(base):
    if base=='A':
        return 'U'
    elif base=='T':
        return 'A'
    elif base=='G':
        return 'C'
    elif base=='C':
        return 'G'
