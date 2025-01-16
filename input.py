import re, sys
def input_user():
    input_string = input("Veuillez entrer votre opération : ").replace(" ", "")
    clean_string = re.findall(r'(?:[0-9.]+)|(?:[+/*%\(\)-])', input_string) # /!\ this regex accept a number 10.4.5.6.6

    try:
        if len(clean_string) < 1: # Check if input is empty
            raise Exception("Vous n'avez pas entré d'opération")
    except Exception as message:
        print(message)

    for element in clean_string:
        try:
            test = re.findall(r"\.+", element) # Correct clean_string in case a number 10.4.5.6 is entered
            if len(test) > 1:
                print(f"{element} n'est pas un nombre !") 
        except Exception:
            pass

    try:
        match = re.search(r'(?:[^0-9.+/*%\(\)-]+)', input_string)
        if bool(match):
            raise Exception(f"Vous avez une entrée incorrecte : {match.group()}")
        return clean_string
    except Exception as message:
        print(message)
        # return None
        sys.exit(1)


    #TODO : raise exception if input doesn't start with number or + or -
    #TODO : max size of list
        # print(clean_string)

    

# input_user()

test =  input_user()
# blabla = "".join(test)
# print(test)
# print(blabla)