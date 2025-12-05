import random

symbols = "ATCG"
length = 8

def random_gen(dna_baseR):
    dna_baseR.clear()
    dna_baseR = random.choices(symbols, k=length)
    random.shuffle(dna_baseR)
    return dna_baseR