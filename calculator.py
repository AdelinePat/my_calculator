import re
import os

os.system('cls')
def u_input(): #demand mathematical expression from user

    

    start=input("{:>100}".format("type in your calculation ('q' to power off)>>")).strip().upper()

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
                case "Q":
                    pass
                case _:
                    print(f"{element} ain't no operator bruh", end="\r")
                    continue
        
    if operationB[0].isnumeric()==False:
        match operationB[0]:
            case '+':
                operationA.insert(0, float(0))
                
            case '-':
                operationA.insert(0, float(0))
            case 'Q':
                print("{:>85}".format("power off..."))
                exit()    
            case _:
                print(f"DON'T START WITH THAT DISGUSTING {operationB[0]}")
    
    
    return operationA 


#############operation received process below

def addition(operation): #for addition
    
    while len(operation)>1 and '+' in operation:
        for element in operation:
            if element=='+':
                index_of_plus=operation.index(element)
                try: #handle out of range errors, happens when 2 operators or more are used and one of them is * or / and the other is + or -
                    operation.insert(index_of_plus, operation[index_of_plus-1]+operation[index_of_plus+1])
                    index_of_plus+=1
                
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-2)
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
                try: #handle out of range errors, happens when 2 operators or more are used and one of them is * or / and the other is + or -
                    operation.insert(index_of_plus, operation[index_of_plus-1]-operation[index_of_plus+1])
                    index_of_plus+=1
                
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-2)
                    index_of_plus-=1
                    operation.pop(index_of_plus)
                except IndexError:
                    operation.insert(1, '-')
                    operation.pop(index_of_plus+1)
    
    return operation

#subtraction complete

def multiplication(operation):
    
    while len(operation)>1 and '*' in operation:
        for element in operation:
            if element=='*':
                index_of_plus=operation.index(element)
                
                operation.insert(index_of_plus, operation[index_of_plus-1]*operation[index_of_plus+1])
                index_of_plus+=1
                operation.pop(index_of_plus+1)
                operation.pop(index_of_plus-2)
                index_of_plus-=1
                operation.pop(index_of_plus)
    
    return operation

#multiplication complete


def division(operation):
    while len(operation)>1 and '/' in operation:
        for element in operation:
            if element=='/':
              
                try:
                    index_of_plus=operation.index(element)

                    operation.insert(index_of_plus, operation[index_of_plus-1]/operation[index_of_plus+1])
                    index_of_plus+=1
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-2)
                    index_of_plus-=1
                    operation.pop(index_of_plus)
                except ZeroDivisionError:
                    print("Cannot divide by zero. could destroy the universe.")
                    main()
                    break
    
    return operation

#division complete

def modulo(operation):
    while len(operation)>1 and '%' in operation:
        for element in operation:
            try:
                if element=='%':
                    index_of_plus=operation.index(element)
                    operation.insert(index_of_plus, operation[index_of_plus-1]%operation[index_of_plus+1])
                    index_of_plus+=1
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-2)
                    index_of_plus-=1
                    operation.pop(index_of_plus)
            except ZeroDivisionError:
                    print("Cannot divide by zero. could destroy the universe.")
                    main()
                    break

    
    return operation
    

#modulo complete



def main():
    try:
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
            print("{:>80}".format(str(result)))
    except UnboundLocalError:
        print("{:>85}".format("result unavailable"))
        main()

main()