import re
def input_user():
    input_string = input("Veuillez entrer votre opération : ").replace(" ", "")
    clean_string = re.findall(r'(?:\d+)|(?:[+/*%-])', input_string)
    # clean_string = re.findall(r'(?:\d+)|(?:[+/*%\(\)-])', input_string) # regex with () 

    match = re.search(r'(?:[^0-9+/*%\(\)-]+)', input_string)

    if bool(match):
        print(f"Vous avez une entrée incorrecte : {match.group()}")
    print(clean_string)
    
input_user()
        