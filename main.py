import random
import DNA_func

app_on = 1
symbols = "ATCG"
password_length = 8
dna_base = []
while app_on > 0:
    correct_data = True
    type_work = input("Enter \"R\" To Randomly Generate DNA Base, Otherwise Enter Any Character: ")
    if type_work == "R" or type_work == "r":
        dna_base.clear()
        dna_base = random.choices(symbols, k=password_length)
        random.shuffle(dna_base)
    
    else:
        dna_base.clear()
        enter_dna_base = input("Enter DNA Base(Only In Uppercase): ")
        for a in enter_dna_base:
            if a in ('A', 'T', 'C', 'G'):
                dna_base.append(a)
            else:
                print("Error! You Enter Wrong Data")
                correct_data = False
                break
    
    if correct_data:
        print(f"Result: {DNA_func.make_dna(dna_base)}")

    user_input = input("Enter 1 To Continue, Or Enter 0: ")

    try:
        app_on = int(user_input)
    except ValueError:
        print("Invalid input! Not an integer. Breaking loop.")
        break
