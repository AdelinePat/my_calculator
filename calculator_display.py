"""
print settings to generate calculator interface with special
characters and ansi escape sequencies
"""
calc_padding_left = 20
calc_padding_top = 1
calc_width = 28
historic_width = 33
historic_print_width = historic_width//2-2

calc_box = {
    "vertical" : "│",
    "horizontal" : "─",
    "vertical_bis" : "║",
    "horizontal_bis" : "═",

    "vertical_>" : "├",
    "vertical_<" : "┤",
    "horizontal_^" : "┴",
    "horizontal_v" : "┬",
    "cross_+" : "┼",

    "horizontal_bis_>" : "╞",
    "horizontal_bis_<" : "╡",
    "vertical_bis_v" : "╥",
    "vertical_bis_<" : "╣",
    "vertical_bis_^" : "╨",

    "angle_tl" : "╭",
    "angle_tr" : "╮",
    "angle_bl" : "╰",
    "angle_br" : "╯",
}

cursor = {
    "save" : "\033[s",
    "load" : "\033[u",

    "line_clear" : "\033[2K",
    "light_line_clear" : "\033[0K",
    "light_clear" : "\033[0J",
    "heavy_clear" : "\033[1;0H\033[0J",

    "bold_start" : "\033[1m",
    "dim_start" : "\033[2m",
    "bold_dim_end" : "\033[22m",

    "underline_start" : "\033[4m",
    "underline_end" : "\033[24m",

    "calc_box_style_start" : "\033[0;1;38;5;129m",
    "historic_data_style_start" : "\033[0;1;2;38;5;82m",
    "results_data_style_start" : "\033[0;1;38;5;82m",

    "instructions_style_start" : "\033[0;37m",
    "result_message_style_start" : "\033[0;1;37m",
    "error_message_style_start" : "\033[0;6;1;31m",

    "style_finish" : "\033[0m"
    # "color_end" : "\033[39m",
    # "red_start" : "\033[31m",
}
def cursor_line(y,x=0):
    coordinate = "\033[" + str(y+ calc_padding_top) + ";" + str(x) + "H"
    return coordinate

def clear_print():
    print(f"{cursor["heavy_clear"]}",
        sep="", end="", flush=True)

'''
    print calculator interface based on settings to host data
    each cursor_line consists of 1 space then 1 separator (changes
    when historic and text interface share the same line)
'''
def setup_printable_fields():
    print(
        f"{cursor['calc_box_style_start']}",

        f"{cursor_line(1)}{" ":^{calc_padding_left}}{calc_box['angle_tl']}",
        f"{"":{calc_box['horizontal']}^{calc_width}}{calc_box['vertical_bis_v']}",
        f"{"":{calc_box['horizontal']}^{historic_width}}{calc_box['angle_tr']}",
        f"{cursor['light_line_clear']}",

        f"{cursor_line(2)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",

        f"{cursor_line(3)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{cursor['result_message_style_start']}{" Résultat :":<{calc_width}}",
        f"{cursor['calc_box_style_start']}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(4)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{cursor['dim_start']}{"":{calc_box['horizontal']}^{historic_width}}",
        f"{cursor['bold_dim_end']}{cursor['bold_start']}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(5)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(6)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(7)}{" ":^{calc_padding_left}}{calc_box['horizontal_bis_>']}",
        f"{"":{calc_box['horizontal_bis']}^{calc_width}}{calc_box['vertical_bis_<']}",
        f"{cursor['dim_start']}{"":{calc_box['horizontal']}^{historic_width}}",
        f"{cursor['bold_dim_end']}{cursor['bold_start']}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(8)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(9)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(10)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{cursor['dim_start']}{"":{calc_box['horizontal']}^{historic_width}}",
        f"{cursor['bold_dim_end']}{cursor['bold_start']}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(11)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(12)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{cursor['instructions_style_start']}{"Entrez votre calcul":^{calc_width}}",
        f"{cursor['calc_box_style_start']}{calc_box['vertical_bis']}",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(13)}{" ":^{calc_padding_left}}{calc_box['vertical_>']}",
        f"{"":{calc_box['horizontal']}^{calc_width}}{calc_box['vertical_bis_^']}",
        f"{"":{calc_box['horizontal']}^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(14)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}} ",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(15)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}} ",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(16)}{" ":^{calc_padding_left}}{calc_box['vertical']}",
        f"{" ":^{calc_width}} ",
        f"{" ":^{historic_width}}{calc_box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(17)}{" ":^{calc_padding_left}}{calc_box['angle_bl']}",
        f"{"":{calc_box['horizontal']}^{calc_width}}{calc_box['horizontal']}",
        f"{"":{calc_box['horizontal']}^{historic_width}}{calc_box['angle_br']}",
        f"{cursor['light_clear']}",

        f"{cursor['style_finish']}", sep="", end="", flush=True
        )

"""
data display within blank fields
"""
def historic_data_print(historic):
    for row in range(0,4):
        x_coord = row*3+3
        y_coord = calc_padding_left+calc_width+4
        if type(historic[row][1]) == float and historic[row][1] != "":
            print(
                f"{cursor_line(x_coord,y_coord)}{cursor['historic_data_style_start']}",
                f"{historic[row][0][0:historic_print_width-2]+" =":<{historic_print_width}} ",
                f"{historic[row][1]:{historic_print_width},.11}".replace(","," ").replace(".",","),
                f"{cursor['style_finish']}", sep="", end="", flush=True)
        elif historic[row][1] != "":
            print(
                f"{cursor_line(x_coord,y_coord)}{cursor['historic_data_style_start']}",
                f"{historic[row][0][0:historic_print_width]+" =":<{historic_print_width}} ",
                f"{historic[row][1][0:historic_print_width]:>{historic_print_width}}",
                f"{cursor['style_finish']}", sep="", end="", flush=True)

def result_data_print(calc_result):
    if type(calc_result) == float:
        print(
            f"{cursor_line(5, calc_padding_left+2)}{cursor['results_data_style_start']}",
            f"{calc_result:{calc_width-3},}".replace(","," ").replace(".",","),
            f"{cursor['style_finish']}", sep="", end="", flush=True)
    else:
        print(
            f"{cursor_line(5, calc_padding_left+2)}{cursor['results_data_style_start']}",
            f"{str(calc_result):>{calc_width-3}}{cursor['style_finish']}",
            sep="", end="", flush=True)

def calc_input_data_print(last_input):
    print(
        f"{cursor_line(9, calc_padding_left+3)}{cursor['dim_start']}",
        f"{last_input[:calc_width-6]:>{calc_width-4}}",
        f" {"=" if last_input != "" else " "}{cursor['style_finish']}",

        sep="", end="", flush=True)
    return input(f"{cursor_line(10,calc_padding_left+4)}\033[8n")

"""
errors display in bottom field, clear field
"""
def error_1_first_operator_print():
    print(
        f"{cursor_line(15,calc_padding_left+2)}{cursor['error_message_style_start']}",
        f"{"L'opération doit commencer par +, - ou un nombre !":^{calc_width+1+historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_onlynumber_print():
    print(
        f"{cursor_line(15,calc_padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Insérez un calcul !":^{calc_width+1+historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_divisionbyzero_print():
    print(
        f"{cursor_line(15,calc_padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Impossible de diviser par 0 !":^{calc_width+1+historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)

def error_clear_print():
    print(
        f"{cursor_line(15,calc_padding_left+1)}{" ":^{calc_width+1+historic_width}}",
        sep="", end="", flush=True)
    

def error_incorrect_input_print(element):

    message = f"Votre entrée {element} est incorrecte !"
    print(
        f"{cursor_line(15,calc_padding_left+2)}{cursor['error_message_style_start']}",
        f"{message:^{calc_width+1+historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)
    

def error_multiple_operators_print():
    print(
        f"{cursor_line(15,calc_padding_left+2)}{cursor['error_message_style_start']}",
        f"{"Vous avez 2 opérateurs consécutifs !":^{calc_width+1+historic_width}}",
        f"{cursor['style_finish']}", sep="", end="", flush=True)