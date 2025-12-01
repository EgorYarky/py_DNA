import random
coplimentary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',}
symbols = "ATCG"
password_length = 8
app_on = 1
while app_on > 0:
    random_dna_base = random.choices(symbols, k=password_length)
    random.shuffle(random_dna_base)
    #print(f"The Random DNA Base: {random_dna_base}")
    #dna_base = ['A', 'C', 'A', 'G', 'T', 'T',]

    def make_dna(base):
        coplimentary_dna = []
        count = 0
        for a in base:
            coplimentary_dna.append(random_dna_base[count])
            coplimentary_dna.append(coplimentary[a])
            count = count + 1
            
        return coplimentary_dna
        
    print(f"Result: {make_dna(random_dna_base)}")
    app_on = int(input("Enter 1 To Countinue, Or Enter 0: "))
