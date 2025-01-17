import re

def blank_input_error(operation_list): 
    try:
        if operation_list == []:
            raise Exception()
        return operation_list
    except Exception:
        return "error_3_blankinput"    

def illegal_entry_input(operation_list, input_user_string):
    try:
        match_input = re.search(r'(?:[^0-9.+/*%\(\)-]+)', input_user_string)
        if bool(match_input):
            raise Exception()
        return operation_list   
    except Exception:
        return "error_5_illegalentry"

def ip_adress_is_not_number(element):
    try:
        test = re.findall(r"\.+", element) # Correct operation_list in case a number 10.4.5.6 is entered
        if len(test) > 1:
            raise Exception()
    except Exception:
        return "error_4_incorrectnumeral"
    
    
"""
Search for / followed by / , insert "//" to enable euclidean division in calculation 
remove individual / from operation_list

Else raise exception
"""
def is_operation_euclidean(element, operation_list):
        operator_list = ["+", "-", "/", "//", "%", "*"]
        try:
            if element in operator_list and operation_list[operation_list.index(element)+1] in operator_list:
                if element == "/" and operation_list[operation_list.index(element)+1] == "/":
                    index_division = operation_list.index(element)
                    operation_list.insert(index_division+2, "//")
                    operation_list.pop(index_division+1)
                    operation_list.pop(index_division)
                    return operation_list
                else:
                    raise Exception()
        except Exception:
            return "error_2_multipleoperators"