import DNA_func
import random_generator

app_on = 1
dna_base = []
while app_on > 0:
    correct_data = True
    type_work = input("Enter \"R\" To Randomly Generate DNA Base, Otherwise Enter Any Character: ")
    if type_work == "R" or type_work == "r":
        dna_base = random_generator.random_gen(dna_base)
    
    else:
        dna_base.clear()
        enter_dna_base = input("Enter DNA Base: ")
        enter_dna_base = enter_dna_base.upper()
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
