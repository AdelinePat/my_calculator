import re
import os

os.system('cls')
def u_input(): #demand mathematical expression from user

    

    start=input("type in your calculation ('q' to power off)>> ").strip()

    operationB=re.findall(r"[\d]+|[\D]", start)

    operationA=[]

    for element in operationB:
        if element.isnumeric():
            operationA.append(float(element))
        else:
            match element:
                case "+":
                    operationA.append(element)
                case "-":
                    operationA.append(element)
                case "*":
                    operationA.append(element)
                case "/":
                    operationA.append(element)
                case "%":
                    operationA.append(element)
                case "(":
                    operationA.append(element)
                case ")":
                    operationA.append(element)
                case "q":
                    pass
                case _:
                    print(f"{element} ain't no operator bruh")
                    continue
        
    if operationB[0].isnumeric()==False:
        match operationB[0]:
            case '+':
                operationA.insert(0, float(0))
                
            case '-':
                operationA.insert(0, float(0))
            case 'q':
                print("powering off...")
                exit()    
            case _:
                print(f"DON'T START WITH THAT DISGUSTING {operationB[0]}")
                operationA.pop(0)
    
    
    return operationA 


#############operation received process below

def addition(operation): #for addition
    
    while len(operation)>1 and '+' in operation:
        for element in operation:
            if element=='+':
                index_of_plus=operation.index(element)
                try:
                    operation.insert(0, operation[index_of_plus-1]+operation[index_of_plus+1])
                    index_of_plus+=1
                
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-1)
                    index_of_plus-=1
                    operation.pop(index_of_plus)
                except IndexError:
                    operation.insert(1, '+')
                    operation.pop(index_of_plus+1)
                
    return operation

#addition complete ^

def subtraction(operation):
    
    while len(operation)>1 and '-' in operation:
        for element in operation:
            if element=='-':
                index_of_plus=operation.index(element)
                try:
                    operation.insert(0, operation[index_of_plus-1]-operation[index_of_plus+1])
                    index_of_plus+=1
                
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-1)
                    index_of_plus-=1
                    operation.pop(index_of_plus)
                except IndexError:
                    operation.insert(1, '-')
                    operation.pop(index_of_plus+1)
    
    return operation

#substraction complete

def multiplication(operation):
    
    while len(operation)>1 and '*' in operation:
        for element in operation:
            if element=='*':
                index_of_plus=operation.index(element)
                operation.insert(0, operation[index_of_plus-1]*operation[index_of_plus+1])
                index_of_plus+=1
                operation.pop(index_of_plus+1)
                operation.pop(index_of_plus-1)
                index_of_plus-=1
                operation.pop(index_of_plus)
    
    return operation

#multiplication complete


def division(operation):
    while len(operation)>1 and '/' in operation:
        for element in operation:
            if element=='/':
                index_of_plus=operation.index(element)
                operation.insert(0, operation[index_of_plus-1]/operation[index_of_plus+1])
                index_of_plus+=1
                operation.pop(index_of_plus+1)
                operation.pop(index_of_plus-1)
                index_of_plus-=1
                operation.pop(index_of_plus)
    
    return operation

#division complete

def modulo(operation):
    while len(operation)>1 and '%' in operation:
        for element in operation:
            if element=='%':
                index_of_plus=operation.index(element)
                operation.insert(0, operation[index_of_plus-1]%operation[index_of_plus+1])
                index_of_plus+=1
                operation.pop(index_of_plus+1)
                operation.pop(index_of_plus-1)
                index_of_plus-=1
                operation.pop(index_of_plus)
    
    return operation
    

#modulo complete



def main():
    while True:
        operation=u_input()
        while len(operation)>1:

            if '*' in operation:
                result=multiplication(operation)
            elif '/' in operation:
                result=division(operation)
            elif '%' in operation:
                result=modulo(operation)
            else:
                for element in operation:
                    match element:
                        case '+':
                            result=addition(operation)
                        case '-':
                            result=subtraction(operation)
        print(result)

main()