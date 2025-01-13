import re
def input_user():
    input_string = input("Veuillez entrer votre opération : ")
    numbers = re.findall(r'\d+', input_string)
    operators = re.findall(r'\D', input_string)
    operators.append("") # adding one caracter to the list so length of numbers and operators are equals

    new_list_numbers = []
    for number in numbers:
        number = int(number)
        new_list_numbers.append(number)

    new_string = []
    for index in range(len(new_list_numbers)):
        new_string.append(new_list_numbers[index])
        new_string.append(operators[index])
    new_string.pop() # removing empty space at the end
    print(new_string)
input_user()






"""
# def evaluate_expression(arr):
#     expression = ''.join(arr)
#     result = eval(expression)
#     return result
# arr = [input("number : "), input("operator :"), input("number : ")]
# result = evaluate_expression(arr)
# print(result)  # Output: 4

# arr = ['(', '1', '6', '*', '0', ')', '+', '(', '1', '6', '*', '1', ')', '+', '5']
# result = evaluate_expression(arr)
# print(result)  # Output: """
"""
def test():
    # calcul = ['(', '1', '6', '*', '0', ')', '+', '(', '1', '6', '*', '1', ')', '+', '5']
    calcul = input("veuillez entrer votre opération : ")
    line = []
    for caracter in range(len(calcul)):
        # while True:
        #     try: test = int(calcul[caracter])
        #     except Exception:
        #         break
        #     calcul[caracter] = int(calcul[caracter])
        #     break
        # if calcul[caracter] == re.findall(r'\d+', calcul[caracter]):
        #     calcul[caracter] = int(calcul[caracter])

        while True:
            try: test = int(calcul[caracter])
            except Exception:
                calcul[caracter]
                break
            number = int(calcul[caracter])
            break

        if calcul[caracter] == number:
            # ligne += number
            line.append(number)
            print(number)
        else:
            line.append(calcul[caracter])

        # elif calcul[caracter] == operator:
        #     line.append(operator)

    for caracter in line:
        match caracter:
            case "+":
                caracter="+"
            case re.findall(r'\d+', caracter):
                caracter = int(caracter)
    result = line
    print(line)
    # print(result)
"""

