from operation_list import configure_input, add_first_operand, update_operation
from operations import multiplication, division, modulo, addition, soustraction, euclidean, equal

def calculation(operation): # operation is operation_list
    
    while len(operation) > 1:
        
        operation = add_first_operand(operation) # add 0 at the beginning of the list if the operation_list starts with an operator
        if operation == "error_1_firstoperand":
            return "error_1_firstoperand"
        while "*" in operation or "/" in operation or "%" in operation or "//" in operation:
            for element in operation:
                match element:
                    case "*":
                        result = multiplication(operation)

                    case "//":
                        try:
                            if operation[operation.index(element)+1] == "0":
                                raise ZeroDivisionError()
                            result = euclidean(operation)
                        except ZeroDivisionError:
                            return "error_0_divisionbyzero"
                        
                    case "/":
                        try:
                            if operation[operation.index(element)+1] == "0":
                                raise ZeroDivisionError()
                            result = division(operation)
                        except ZeroDivisionError:
                            return "error_0_divisionbyzero"
                    
                    case "%":
                        try:
                            if operation[operation.index(element)+1] == "0":
                                raise ZeroDivisionError()
                            result = modulo(operation)
                        except ZeroDivisionError:
                            return "error_0_divisionbyzero"


        while "+" in operation or "-" in operation:
            for element in operation:
                match element:
                    case "+":
                        result = addition(operation)
                    case "-":
                        result = soustraction(operation)
    if len(operation) == 1:
        result = equal(operation)
    return result

"""
Search () , create a sub-list from inside parenthesis 
Calculate operations inside sub-list, insert result inside original-list
Remove all items inside sub-list + parenthesis from original-list
"""

def sub_operation_treatment(operation):
    while "(" in operation and ")" in operation:
        start_index = operation.index("(")
        end_index = operation.index(")")
        range_of_sub_operation = slice(start_index, end_index+1)
        sub_operation = operation[range_of_sub_operation]
    
        sub_operation.pop(-1) # deleting parenthesis ")" from sub_operation list
        sub_operation.pop(0) # deleting parenthesis "(" from sub_operation list
     
        sub_calculation = calculation(sub_operation)
        match sub_calculation:
            case "error_0_divisionbyzero":
                return "error_0_divisionbyzero"
            case "error_1_firstoperand":
                return "error_1_firstoperand"
        for index in reversed(range(start_index, end_index+1)):
            operation.pop(index)

        operation.insert(start_index, sub_calculation)



""" DEBUG CALCULATOR """
# input_user_string = input("Veuillez entrer votre opération : ")
# clean_input = configure_input(input_user_string)
# sub_operation_treatment(clean_input)
# final_result = calculation(clean_input)
# print(f"résultat final : {final_result}")
