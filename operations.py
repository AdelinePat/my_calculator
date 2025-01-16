
from operation_list import configure_input, update_operation

import sys 
def multiplication(operation):
    multiplication_index = operation.index("*")
    result = float(operation[multiplication_index-1])*float(operation[multiplication_index+1])
    update_operation(operation, multiplication_index, result)

    return result

def division(operation):
    division_index = operation.index("/")
    try:
        if operation[division_index+1] == "0":
            raise ZeroDivisionError("La division par 0 est impossible")
        result = float(operation[division_index-1])/float(operation[division_index+1])
        update_operation(operation, division_index, result)
        return result
      
    except ZeroDivisionError as message:
        print(message)
        return configure_input(input("Veuillez entrer votre opération : "))

def modulo(operation):
    modulo_index = operation.index("/")
    try:
        if operation[modulo_index+1] == "0":
            raise ZeroDivisionError("La division par 0 est impossible")
        result = float(operation[modulo_index-1])/float(operation[modulo_index+1])
        update_operation(operation, modulo_index, result)   
        return result
        
    except ZeroDivisionError as message:
        print(message)
        return configure_input(input("Veuillez entrer votre opération : "))

def addition(operation):
    addition_index = operation.index("+")
    result = float(operation[addition_index-1])+float(operation[addition_index+1])
    update_operation(operation, addition_index, result)

    return result

def soustraction(operation):
    soustraction_index = operation.index("-")
    result = float(operation[soustraction_index-1])-float(operation[soustraction_index+1])
    update_operation(operation, soustraction_index, result)

    return result
