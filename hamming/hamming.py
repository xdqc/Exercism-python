def distance(dna1, dna2):
    if len(dna1)!=len(dna2):
        raise ValueError('Two strand with different length.')
    return sum(x!=y for x,y in zip(dna1, dna2))
