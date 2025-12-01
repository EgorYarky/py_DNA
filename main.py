import random
coplimentary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',}
symbols = "ATCG"
password_length = 8
random_dna_base = random.choices(symbols, k=password_length)
random.shuffle(random_dna_base)
print(f"The Random DNA Base: {random_dna_base}")
#dna_base = ['A', 'C', 'A', 'G', 'T', 'T',]

def make_dna(base):
    coplimentary_dna = []
    for a in base:
        coplimentary_dna.append(coplimentary[a])
        
    return coplimentary_dna


print(make_dna(random_dna_base))
