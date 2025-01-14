import re
from input import input_user

def start_with(clean_input):
    start_with_operator = []
    start_with_number = []
    for element in clean_input:
        try:
            test = float(clean_input[0])
            start_with_number.append(element)
            pass
        except Exception:
            start_with_operator.append(element)
    return start_with_number, start_with_operator

clean_input = input_user()
start_with_number = start_with(clean_input)[0]
start_with_operator = start_with(clean_input)[1]

print(start_with_number)
print(start_with_operator)

def calculation(start_with_number, start_with_operator):
    if start_with_number:
        for index in range(len(start_with_number)):
            for element in start_with_number[1::2]:
                result = 0
                print((start_with_number[index-1]))
                match element:
                    case "+":
                        print("addition")
                        result = float(start_with_number[index]) + float(start_with_number[2])
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
        if start_with_operator[0] != "+" and start_with_operator[0] != "-" :
            print(f"Vous ne pouvez pas commencer votre opération par {start_with_operator[0]}")
        else:
            start_with_operator.insert(0, "0")
            print(f"nouvelle version {start_with_operator}")
            # for element in start_with_operator[1::2]:
            #     result = 0
            #     match element:
            #         case "+":
            #             print("addition")
            #             result = float(start_with_operator[0]) + float(start_with_operator[2])
            #             print(result)
            #         case "-":
            #             print("soustraction")
            #             result = float(start_with_operator[0]) - float(start_with_operator[2])
            #             print(result)
            #         case "*":
            #             print("multiplication")
            #             result = float(start_with_operator[0]) * float(start_with_operator[2])
            #             print(result)
            #         case "/":
            #             print("division")
            #             result = float(start_with_operator[0]) / float(start_with_operator[2])
            #             print(result)
            #         case "%":
            #             print("modulo")
            #             result = float(start_with_operator[0]) % float(start_with_operator[2])
            #             print(result)
            #         case _:
            #             print("il y a une erreur dans l'opération")
            # for element in start_with_operator[::2]:
            #     print(f"nombre de operator : {element}")
            #     result = 0
            # match element:
            #     case "+":
            #         print("addition")
            #         result += float(start_with_number[1])
            #         print(result)
            #     case "-":
            #         print("soustraction")
            #         result -= float(start_with_number[1])
            #         print(result)
            #     case "*":
            #         print("multiplication")
            #         result *= float(start_with_number[1])
            #         print(result)
            #     case "/":
            #         print("division")
            #         result /= float(start_with_number[1])
            #         print(result)
            #     case "%":
            #         print("modulo")
            #         result %= float(start_with_number[1])
            #         print(result)
            #     case _:
            #         print("il y a une erreur dans l'opération")
            
# calculation(start_with_number, start_with_operator)