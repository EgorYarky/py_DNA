coplimentary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',}

dna_base = ['A', 'C', 'A', 'G', 'T', 'T',]

def make_dna(base):
    for a in base:
        print(coplimentary[a])
        print(a)

make_dna(dna_base)
