import random
coplimentary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',}
app_on = 1
symbols = "ATCG"
password_length = 8
dna_base = []
while app_on > 0:
    type_work = input("Enter \"R\" To Randomly Generate DNA Base, Otherwise Enter Any Character: ")
    if type_work == "R" or type_work == "r":
        dna_base.clear()
        dna_base = random.choices(symbols, k=password_length)
        random.shuffle(dna_base)
    
    else:
        dna_base.clear()
        enter_dna_base = input("Enter DNA Base(Only In Uppercase): ")
        for a in enter_dna_base:
            if a == 'A' or a == 'T' or a == 'C' or a == 'G':
                dna_base.append(a)
            else:
                print("Error! You Enter Wrong Data")
                break

    def make_dna(base):
        coplimentary_dna = []
        count = 0
        for a in base:
            coplimentary_dna.append(dna_base[count])
            coplimentary_dna.append(coplimentary[a])
            count = count + 1
            
        return coplimentary_dna
        
    print(f"Result: {make_dna(dna_base)}")
    
    user_input = input("Enter 1 To Continue, Or Enter 0: ")
    try:
        app_on = int(user_input)
    except ValueError:
        print("Invalid input! Not an integer. Breaking loop.")
        break
