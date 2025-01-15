# import calculator_display as display
# cursor = display.cursor
# cursor_line = display.cursor_line

print_fr_value = ("Premier","Deuxième","Troisième",)
print_fr_type = (" nombre"," opérateur")

calc_padding = 15
calc_width = 32
historic_width = 32

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

    "bold_pink_start" : "\033[1;38;5;13m",
    "bold_green_start" : "\033[1;38;5;82m",
    "red_start" : "\033[31m",
    "white_start" : "\033[37m",
    "color_end" : "\033[39m",
    "style_finish" : "\033[0m"
}
def cursor_line(y,x=0):
    coordinate = "\033[" + str(y) + ";" + str(x) + "H"
    return coordinate

def clear_print():
    print(f"{cursor["heavy_clear"]}",
        sep="", end="", flush=True)

def setup_print():
    print(
        f"{cursor['bold_pink_start']}",
        f"{cursor_line(1)}{" ":^{calc_padding}} {"":_^{calc_width+1+historic_width}}",
        f"{cursor_line(2)}{" ":^{calc_padding}}/{" ":^{calc_width}}|{" ":^{historic_width}}\\",
        f"{cursor_line(3)}{" ":^{calc_padding}}⎸",
        f"{cursor['bold_green_start']}{" Résultat :":<{calc_width}}",
        f"{cursor['bold_pink_start']}|{" ":^{historic_width}}⎹",
        f"{cursor_line(4)}{" ":^{calc_padding}}⎸{" ":^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(5)}{" ":^{calc_padding}}⎸{" ":^{calc_width}}|{"":_^{historic_width}}⎹",
        f"{cursor_line(6)}{" ":^{calc_padding}}\\{"":_^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(7)}{" ":^{calc_padding}}/{" ":^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(8)}{" ":^{calc_padding}}⎸{" ":^{calc_width}}|{"":_^{historic_width}}⎹",
        f"{cursor_line(9)}{" ":^{calc_padding}}⎸{" ":^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(10)}{" ":^{calc_padding}}⎸{" ":^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(11)}{" ":^{calc_padding}}⎸",
        f"{cursor['white_start']}{"Entrez votre calcul":^{calc_width}}",
        f"{cursor['bold_pink_start']}|{"":_^{historic_width}}⎹",
        f"{cursor_line(12)}{" ":^{calc_padding}}\\{"":_^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(13)}{" ":^{calc_padding}}/{" ":^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(14)}{" ":^{calc_padding}}⎸{" ":^{calc_width}}|{" ":^{historic_width}}⎹",
        f"{cursor_line(15)}{" ":^{calc_padding}}\\{"":_^{calc_width}}|{"":_^{historic_width}}/",
        f"{cursor['style_finish']}", sep="", end="", flush=True
        )

def historic_print():
    print("")

def result_print(calc_result):
    print(
        f"{cursor_line(5, calc_padding+2)}{cursor['bold_green_start']}",
        f"{float(calc_result):{calc_width-3},}\
{cursor['style_finish']}".replace(","," ").replace(".",","),
        sep="", end="", flush=True)

def calc_terminal_print(last_input):
    print(
        f"{cursor_line(8, calc_padding+2)}{cursor['dim_start']}",
        f"{last_input[:calc_width-5]:>{calc_width-5}}",
        f" {"=" if last_input != "" else " "}{cursor['style_finish']}",

        sep="", end="", flush=True)
    return input(cursor_line(9,calc_padding+4))

def error_onlynumber_print():
    print(
        f"{cursor_line(15,calc_padding+2)}{cursor['bold_red_start']}",
        f"{"Insérez un calcul !":^{calc_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_divisionbyzero_print():
    print(
        f"{cursor_line(15,calc_padding+2)}{" ":^{calc_padding}}{cursor['bold_start']}",
        f"⎸{cursor['red_start']}{"Impossible de diviser par 0 !":^{calc_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_clear_print():
    print(
        f"{cursor_line(15,calc_padding+1)}{" ":^{calc_width}}",
        sep="", end="", flush=True)