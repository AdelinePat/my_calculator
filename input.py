import re
def input_user():
    input_string = input("Veuillez entrer votre opération : ").replace(" ", "")
    if bool(re.search(r'\d', input_string)) == False:
        print("Vous n'avez entré aucun chiffre")
        return input_user()
    else:
        numbers = re.findall(r'\d+', input_string)
        operators = re.findall(r'[+-/*]+', input_string)
        
        new_operators = operators
        new_operators.append("") # adding one caracter to the list so length of numbers and operators are equals

    print(f" ceci est un test de input_string {input_string}")

    new_list_numbers = []
    for number in numbers:
        number = int(number)
        new_list_numbers.append(number)

    new_string = []
    # if len(numbers) >= len(operators):
    print(f"OPERATEUR {operators}")
    print(f"NEW OPERATEUR {new_operators}")
    print(f"NUMBERS {numbers}")
    for index in range(len(new_list_numbers)):
        if bool(re.search(r'^[+-/*]', input_string)):
            new_string.append(operators[index])
            new_string.append(new_list_numbers[index]) 
        else:
            new_string.append(new_list_numbers[index])
            new_string.append(operators[index])
            # new_string.pop() # removing empty space at the end
    
    if new_string[-1] == "":
        new_string.pop()
    # else:
    #     for index in range(len(new_list_numbers)):
    #         new_string.append(operators[index])
    #         new_string.append(new_list_numbers[index])         

    print(f"ceci est la nouvelle liste finie {new_string}")

   
    return new_string
# input_user()


# def check_number():
def check_operator(operation_list):
    for index in range(len(operation_list)):
        result = 0
        if operation_list[index].isnumeric() and operation_list[index+1]%2 != 0:
            match operation_list[index]:
                case "+":
                    result += operation_list[index]
                case "-":
                    result -= operation_list[index]
                case "*":
                    result *= operation_list[index]
                case "/":
                    result /= operation_list[index]
                case "%":
                    result %= operation_list[index]
                case _:
                    print(f"L'opérateur {operation_list[index]} n'est pas valide")
        print(result)

while True:

    calcul_list = input_user()
    # check_operator(calcul_list)