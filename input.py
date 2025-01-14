import re, sys
def input_user():
    input_string = input("Veuillez entrer votre opération : ").replace(" ", "")
    clean_string = re.findall(r'(?:[0-9.]+)|(?:[+/*%\(\)-])', input_string) #TODO /!\ this regex accept a number 10.4.5.6.6
    # clean_string = re.findall(r'((?:[0-9]+).(?:[0-9]+))|(?:[+/*%-])', input_string) #VERSION 2
    # clean_string = re.findall(r'(\d+\.\d+)|(?:[0-9]+)|(?:[+/*%-])', input_string)
    # ((?:[0-9]+).(?:[0-9]+))|(?:[+/*%-])
    
    # clean_string = re.findall(r'(?:\d+)|(?:[+/*%\(\)-])', input_string) # regex with () 

    try:
        match = re.search(r'(?:[^0-9.+/*%\(\)-]+)', input_string)
        if bool(match):
            raise Exception(f"Vous avez une entrée incorrecte : {match.group()}")
        return clean_string
    except Exception as message:
        print(message)
        # return None
        sys.exit(1)

        
        # print(clean_string)

    

# input_user()