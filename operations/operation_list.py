import re
from operations.check_error import blank_input_error, illegal_entry_input, ip_adress_is_not_number, is_operation_euclidean

def configure_input(input_user_string):
    input_user_string = input_user_string.replace(" ", "")
    operation_list = re.findall(r'(?:[0-9.]+)|(?:[+/*%\(\)-])', input_user_string)
    
    operation_list = blank_input_error(operation_list)

    for element in operation_list:
        if ip_adress_is_not_number(element) == "error_4_incorrectnumeral": 
            return "error_4_incorrectnumeral"
        if is_operation_euclidean(element, operation_list) == "error_2_multipleoperators":
            return "error_2_multipleoperators"
    
    operation_list = illegal_entry_input(operation_list, input_user_string)

    return operation_list

'''
Add 0 at the beginning of the list if the operation_list starts with an operator
Return a list starting with a number
'''
def add_first_operand(operation_list):
    try:
        test = float(operation_list[0])
        return operation_list     
    except Exception:
        if operation_list[0] != "+" and operation_list[0] != "-":
            return "error_1_firstoperand"
        else:
            operation_list.insert(0, "0")
            return operation_list

'''
Add result to operation_list, remove both operands and operator
'''
def update_operation(operation_list, operator_index, result):
    operation_list.insert(operator_index+2, result)
    operation_list.pop(operator_index+1)
    operation_list.pop(operator_index)
    operation_list.pop(operator_index-1)

    return operation_list
