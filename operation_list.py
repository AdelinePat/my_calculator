import re, sys
# input_user_string = input("Veuillez entrer votre opération : ")
def configure_input(input_user_string):
    input_user_string = input_user_string.replace(" ", "")
    operation_list = re.findall(r'(?:[0-9.]+)|(?:[+/*%\(\)-])', input_user_string) # /!\ this regex accept a number 10.4.5.6.6

    try:
        if len(operation_list) < 1: # Check if input is empty
            raise Exception("Vous n'avez pas entré d'opération")
    except Exception as message:
        print(message)

    for element in operation_list:
        try:
            test = re.findall(r"\.+", element) # Correct operation_list in case a number 10.4.5.6 is entered
            if len(test) > 1:
                raise Exception(f"{element} n'est pas un nombre !") 
        except Exception as message_1:
            print(message_1)

    try:
        match = re.search(r'(?:[^0-9.+/*%\(\)-]+)', input_user_string)
        if bool(match):
            raise Exception(f"Vous avez une entrée incorrecte : {match.group()}")
        return operation_list
    except Exception as message:
        print(message)
        sys.exit(1)


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
             print(f"Vous ne pouvez pas commencer votre opération par {operation_list[0]}")
             return None
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
