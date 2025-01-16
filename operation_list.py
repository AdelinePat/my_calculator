import re, sys
import calculator_display as display

def configure_input(input_user_string):
    input_user_string = input_user_string.replace(" ", "")
    operation_list = re.findall(r'(?:[0-9.]+)|(?:[+/*%\(\)-])', input_user_string) # /!\ this regex accept a number 10.4.5.6.6
    if input_user_string == "off":
        operation_list = "off"
        return operation_list
    try:
        if len(operation_list) < 1: # Check if input is empty
            raise Exception(display.error_onlynumber_print())
    except Exception as message:
        print(message)
        return configure_input(display.calc_input_data_print(""))

    for element in operation_list:
        try:
            test = re.findall(r"\.+", element) # Correct operation_list in case a number 10.4.5.6 is entered
            if len(test) > 1:
                raise Exception(display.error_incorrect_input_print(element)) # TODO create a function for this error
        except Exception as message_1:
            print(message_1)
            return configure_input(display.calc_input_data_print(""))
        
        """
        Search for / followed by / , insert "//" to enable euclidean division in calculation 
        remove individual / from operation_list

        Else raise exception
        """
        operator_list = ["+", "-", "/", "//", "%", "*"]
        try:
            if element in operator_list and operation_list[operation_list.index(element)+1] in operator_list:
                if element == "/" and operation_list[operation_list.index(element)+1] == "/":
                    index_division = operation_list.index(element)
                    operation_list.insert(index_division+2, "//")
                    operation_list.pop(index_division+1)
                    operation_list.pop(index_division)
                else:
                    raise Exception(display.error_multiple_operators_print())
        except Exception as message_2:
            print(message_2)
            return configure_input(display.calc_input_data_print(""))
        
     
    try:
        match_input = re.search(r'(?:[^0-9.+/*%\(\)-]+)', input_user_string)
        # match_command = re.search(r'(?:^[off]*)', input_user_string)

        if bool(match_input):
            raise Exception(display.error_incorrect_input_print(match_input.group())) # TODO create a function for this error too
        return operation_list
    except Exception as message:
        print(message)
        return configure_input(display.calc_input_data_print(""))


"""
Add 0 at the beginning of the list if the operation_list starts with an operator
Return a list starting with a number
"""
def add_first_operand(operation_list):
    try:
        test = float(operation_list[0])
        return operation_list     
    except Exception:
        if operation_list[0] != "+" and operation_list[0] != "-":
            display.error_1_first_operator_print()
            return configure_input(display.calc_input_data_print(""))
        else:
            operation_list.insert(0, "0")
            return operation_list

""" Add result to operation_list, remove both operands and operator """
def update_operation(operation_list, operator_index, result):
    operation_list.insert(operator_index+2, result)
    operation_list.pop(operator_index+1)
    operation_list.pop(operator_index)
    operation_list.pop(operator_index-1)

    return operation_list
