import calc_display.print_settings as calc
from calc_display.print_settings import cursor_line, cursor
'''
    errors display in bottom field, else happy message
'''
def error_message_print(error_code):
    match error_code:
        case "error_0_divisionbyzero":
            error_0_divisionbyzero_print()
        case "error_1_firstoperand":
            error_1_first_operator_print()
        case "error_2_multipleoperators":
            error_2_multiple_operators_print()
        case "error_3_blankinput":
            error_3_blank_input_print()
        case "error_4_incorrectnumeral":
            error_4_incorrect_numeral_print()
        case "error_5_illegalentry":
            error_5_illegal_entry_print()
        case "error_6_unknown":
            error_6_unknown()
        case _:
            legal_operation_print()

def legal_operation_print():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['happy_message_style_start']}",
        f"{"Ce calcul est possible !":^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_0_divisionbyzero_print():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Impossible de diviser par 0 !":^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_1_first_operator_print():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{"L'opération doit commencer par +, - ou un nombre !":^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_2_multiple_operators_print():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Vous avez 2 opérateurs consécutifs !":^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_3_blank_input_print():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Insérez un calcul !":^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_4_incorrect_numeral_print():
    message = f"Votre entrée contient un nombre incorrect !"
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{message:^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_5_illegal_entry_print():
    message = f"Votre calcul contient une entrée interdite !"
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{message:^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_6_unknown():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Une erreur inconnue est survenue":^{calc.width+1+calc.historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_clear_print():
    print(
        f"{cursor_line(15,calc.padding_left+2)}{" ":^{calc.width+1+calc.historic_width}}",
        sep="", end="", flush=True)