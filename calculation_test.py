import re
from input import input_user

def start_with(clean_input):
    start_with_operator = []
    start_with_number = []
    for element in clean_input:
        try:
            test = int(clean_input[0])
            # print(f"l'opération commence par un nombre {element}")
            start_with_number.append(element)
            pass
        except Exception:
            # print(f"l'opération commence par un opérateur {element}")
            start_with_operator.append(element)
    
    # print(start_with_number)
    # print(start_with_operator)
    return start_with_number, start_with_operator
        # if element == "-" or element == "+":
        #     print("l'opération commence par un opérateur")
        # else:
        #     print("l'opération commence par un nombre")

clean_input = input_user()
start_with_number = start_with(clean_input)[0]
start_with_operator = start_with(clean_input)[1]

def calculation(start_with_number, start_with_operator):
    # print(start_with_number)
    # print(start_with_operator)

    if start_with_number:
        # for number in start_with_number[::2]:
        #     float(number)
        #     # print(f"nombre : {element}")
        #     # print(f"operateur ? {start_with_number[1::2]}")
        #     # print("la liste de nombre n'est pas vide")
        for element in start_with_number[1::2]:
            result = 0
            match element:
                case "+":
                    print("addition")
                    result = float(start_with_number[0]) + float(start_with_number[2])
                    print(result)
                case "-":
                    print("soustraction")
                    result = float(start_with_number[0]) - float(start_with_number[2])
                    print(result)
                case "*":
                    print("multiplication")
                    result = float(start_with_number[0]) * float(start_with_number[2])
                    print(result)
                case "/":
                    print("division")
                    result = float(start_with_number[0]) / float(start_with_number[2])
                    print(result)
                case "%":
                    print("modulo")
                    result = float(start_with_number[0]) % float(start_with_number[2])
                    print(result)
                case _:
                    print("il y a une erreur dans l'opération")


    else:
        if start_with_operator[0] == "/" or start_with_operator[0] == "*" or start_with_operator[0] == "%" :
            print(f"Vous ne pouvez pas commencer votre opération par {start_with_operator[0]}")
            
        else:
            for element in start_with_operator[1::2]:
                print(f"nombre de operator : {element}")
                # for element in start_with_operator[::2]:
                #     print(element)
                
                # print("la liste de nombre n'est pas vide")
calculation(start_with_number, start_with_operator)