import sys
from input import input_user

def add_first_operand(clean_input):
    try:
        test = float(clean_input[0])
        # print(f"list operation = {clean_input}")
        return clean_input     
    except Exception:
        if clean_input[0] != "+" and clean_input[0] != "-":
             print(f"Vous ne pouvez pas commencer votre opération par {clean_input[0]}")
             return None
        else:
            clean_input.insert(0, "0")
            # print(f"list operation operateur = {clean_input}")
            return clean_input
    
clean_input = input_user()
# if clean_input != None:



def update_operation(mylist, operator_index,result):
    mylist.insert(operator_index+2, result)
    mylist.pop(operator_index+1)
    mylist.pop(operator_index)
    mylist.pop(operator_index-1)

def calculation(operation):
    operation = add_first_operand(operation)

    try:
        multiplication_index = operation.index("*")
        result = float(operation[multiplication_index-1])*float(operation[multiplication_index+1])
        update_operation(operation, multiplication_index, result)
        # print(f"list après pop = {operation}")
        
        result = calculation(operation)
        
        # print(f"resultat = {result}")
    except Exception:
        pass
    
    try:
        division_index = operation.index("/")
        if operation[division_index+1] == "0":
            raise ZeroDivisionError("La division par 0 est impossible")
        result = float(operation[division_index-1])/float(operation[division_index+1])
        update_operation(operation, division_index, result)
        # print(f"list après pop = {operation}")

        result = calculation(operation)

        
        # print(result)

    except ZeroDivisionError as message:
        print(message)
        sys.exit(1)
    except Exception:
        pass
        
    try:
        modulo_index = operation.index("%")
        if operation[modulo_index+1] == "0":
            raise ZeroDivisionError("La division par 0 est impossible")
        result = float(operation[modulo_index-1])%float(operation[modulo_index+1])

        update_operation(operation, modulo_index, result)
        # print(f"list après pop = {operation}")

        result = calculation(operation)

        
        # print(result)

    except ZeroDivisionError as message:
        print(message)
        sys.exit(1)
    except Exception:
        pass
    
    if "+" in operation and "-" in operation:
        if operation.index("+") < operation.index("-"):
            addition_index = operation.index("+")
            result = float(operation[addition_index-1])+float(operation[addition_index+1])

            update_operation(operation, addition_index, result)
            # print(f"list après pop = {operation}")

            result = calculation(operation)

        else:
            soustraction_index = operation.index("-")
            result = float(operation[soustraction_index-1])-float(operation[soustraction_index+1])

            update_operation(operation, soustraction_index, result)
            # print(f"list après pop = {operation}")

            result = calculation(operation)

    try:
        addition_index = operation.index("+")
        result = float(operation[addition_index-1])+float(operation[addition_index+1])

        update_operation(operation, addition_index, result)
        # print(f"list après pop = {operation}")

        result = calculation(operation)

        
        # print(result)
    except Exception:
        pass

    try:
        soustraction_index = operation.index("-")
        result = float(operation[soustraction_index-1])-float(operation[soustraction_index+1])

        update_operation(operation, soustraction_index, result)
        # print(f"list après pop = {operation}")

        result = calculation(operation)

        
        # print(result)
    except Exception:
        pass
    
    return result

def sub_operation_treatment(operation):
    while "(" in operation and ")" in operation:
        start_index = operation.index("(")
        end_index = operation.index(")")
        range_of_sub_operation = slice(start_index, end_index+1)
        sub_operation = operation[range_of_sub_operation]
        # print(f"sub operation avant pop : {sub_operation}")
        sub_operation.pop(-1) # deleting parenthesis ")" from sub_operation list
        sub_operation.pop(0) # deleting parenthesis "(" from sub_operation list
        # print(f"sub operation apres pop : {sub_operation}")

        sub_calculation = calculation(sub_operation)
        for index in reversed(range(start_index, end_index+1)):
            operation.pop(index)

        operation.insert(start_index, sub_calculation)
        # print(f"operation dans sub_operation : {operation}")
        

        # operation.insert(start_index)
    # return operation

sub_operation_treatment(clean_input)
final_result = calculation(clean_input)
print(f"résultat final : {final_result}")