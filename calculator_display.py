print_fr_value = ("Premier","Deuxième","Troisième",)
print_fr_type = (" nombre"," opérateur")

cursor = {
    "line_1" : "\033[1;0H",
    "line_2" : "\033[2;0H",
    "line_3" : "\033[3;0H",
    "line_4" : "\033[4;0H",
    "line_5" : "\033[5;0H",
    "line_6" : "\033[6;0H",
    "line_7" : "\033[7;0H",
    "input_xy" : "\033[3;15H",

    "save" : "\033[s",
    "load" : "\033[u",

    "line_clear" : "\033[2K",
    "light_clear" : "\033[0J",
    "heavy_clear" : "\033[1;0H\033[0J",

    "bold_start" : "\033[1m",
    "dim_start" : "\033[2m",
    "bold_dim_end" : "\033[22m",
    "underline_start" : "\033[4m",
    "underline_end" : "\033[24m",

    "red_start" : "\033[31m",
    "style_finish" : "\033[0m"
}
def cursor_line(y,x=0):
    coordinate = "\033[" + str(y) + ";" + str(x) + "H"
    return coordinate

def setup_print():
    print(
        f"{cursor["heavy_clear"]}",
        f"{cursor_line(1)}{cursor['light_clear']} {"":_^36}",
        f"{cursor_line(2)}{cursor['light_clear']}/{" ":^36}\ ",
        f"{cursor_line(4)}{cursor['light_clear']}\{"":_^36}/",
        f"{cursor_line(8)}{cursor['light_clear']}\{"":_^36}/",
        sep="", end="", flush=True
        )

def result_print(calc_result):
    print(
        f"{cursor_line(3)}{cursor['bold_start']}⎸Résultat :{str(calc_result)[:25]:>25} ⎹{cursor['bold_dim_end']}",
        sep="", end="", flush=True)

def calc_terminal_print(calc_line_1_number, calc_line_1_type, calc_line_2):
    print(
        f"{cursor_line(5)}/{cursor['underline_start']}",
        f"{print_fr_value[calc_line_1_number] + print_fr_type[calc_line_1_type][:36]:_^36}",
        f"{cursor['underline_end']}\ ",sep="", end="", flush=True)
    print(
        f"{cursor_line(6)}{cursor['bold_start']}⎸{cursor['bold_dim_end']}",
        f"{cursor['dim_start']}{calc_line_2[:36]:<36}{cursor['bold_dim_end']}",
        f"{cursor['bold_start']}⎹{cursor['bold_dim_end']}",
        sep="", end="", flush=True)
    print(f"{cursor_line(7)}{cursor['bold_start']}⎸{cursor['bold_dim_end']}",
        f"{" ":<36}",
        f"{cursor['bold_start']}⎹{cursor['bold_dim_end']}",
        sep="", end="", flush=True)
    return input(cursor_line(7,2))

def error_onlynumber_print():
    print(
        f"{cursor_line(9)}/{cursor['red_start']}{cursor['bold_start']}",
        f"{"Insérez une valeur numérique !"[:36]:^36}",
        f"{cursor['style_finish']}\{cursor_line(10)}\{"":_^36}/",
        sep="", end="", flush=True)

def error_operators_print():
    print(
        f"{cursor_line(9)}/{cursor['red_start']}{cursor['bold_start']}",
        f"{"Insérez un opérateur (+-/*) !"[:36]:^36}",
        f"{cursor['style_finish']}\{cursor_line(10)}\{"":_^36}/",
        sep="", end="", flush=True)

def error_clear_print():
    print(
        f"{cursor_line(9)}{"":^38}{cursor_line(10)}{"":^38}",
        sep="", end="", flush=True)