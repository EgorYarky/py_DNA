coplimentary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',}

def make_dna(base):
        coplimentary_dna = []
        count = 0
        for a in base:
            coplimentary_dna.append(base[count])
            coplimentary_dna.append(coplimentary[a])
            count = count + 1
            
        return coplimentary_dna