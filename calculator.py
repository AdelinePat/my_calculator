import re
import os

os.system('cls')
def u_input(): #demand mathematical expression from user

    
    print("\033[H")
    start=input("{:>100}".format("type in your calculation ('q' to power off, 'c' to clear)>>")).strip().upper()
    print(f"\033[{1};1H")
    print("\033[K")
    
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
                case "C":
                    pass
                case _:
                    continue
    try:    
        if operationB[0].isnumeric()==False:
            
            match operationB[0]:
                case '+':
                    operationA.insert(0, float(0))
                    
                case '-':
                    operationA.insert(0, float(0))
                case 'Q':
                    print("{:>85}".format("power off..."))
                    exit()
                case 'C':
                    print("\033[0J")   
                    main() 
                case _:
                    print("{:>95}".format(f"{operationB[0]} is invalid, Removed automatically"), "\033[K")
                    #operationA.pop(0)
    except IndexError:
        print("{:>85}".format("your input is empty"))
        main()            
        
    
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
                    if operation[index_of_plus]==operation[index_of_plus+1]:
                        print("{:>85}".format("result unavailable"))
                        main()
                    else:
                        operation.pop(index_of_plus+1)
                except TypeError:
                    print("{:>85}".format("result unavailable"), "\033[K")
                    main()

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
                    if operation[index_of_plus]==operation[index_of_plus+1]:
                        print("{:>85}".format("result unavailable"))
                        main()
                    else:
                        operation.pop(index_of_plus+1)
                except TypeError:
                    print("{:>85}".format("result unavailable"), "\033[K")
                    main()
    
    return operation

#subtraction complete

def multiplication(operation):
    
    while len(operation)>1 and '*' in operation:
        for element in operation:
            if element=='*':
                try:
                    index_of_plus=operation.index(element)
                    
                    operation.insert(index_of_plus, operation[index_of_plus-1]*operation[index_of_plus+1])
                    index_of_plus+=1
                    operation.pop(index_of_plus+1)
                    operation.pop(index_of_plus-2)
                    index_of_plus-=1
                    operation.pop(index_of_plus)
                except (IndexError, TypeError):
                    print("{:>85}".format("result unavailable"), "\033[K")
                    main()
    
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
                    print("{:>105}".format("Cannot divide by zero."))
                    main()
                    break
                except (IndexError, TypeError):
                    print("{:>85}".format("result unavailable"), "\033[K")
                    main()
    
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
                    print("{:>100}".format("Cannot divide by zero."))
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
            print("{:>85}".format(str(result)), "\033[J")
    except UnboundLocalError:
        print("{:>85}".format("result unavailable"))
        main()
    except KeyboardInterrupt:
        print("{:>150}".format("power off..."))
        exit()

main()