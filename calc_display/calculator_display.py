import calc_display.print_settings as calc
from calc_display.print_settings import cursor_line, cursor
"""
data display within blank fields
"""
def historic_data_print(historic):
    for row in range(0,4):
        x_coord = row*3+3
        y_coord = calc.padding_left+calc.width+4
        if type(historic[row][1]) == float and historic[row][1] != "":
            print(
                f"{cursor_line(x_coord,y_coord)}{cursor['historic_data_style_start']}",
                f"{historic[row][0][0:calc.historic_print_width-2]+" =":<{calc.historic_print_width}} ",
                f"{historic[row][1]:{calc.historic_print_width},.11}".replace(","," ").replace(".",","),
                f"{cursor['style_finish']}", sep="", end="", flush=True)
        elif historic[row][1] != "":
            print(
                f"{cursor_line(x_coord,y_coord)}{cursor['historic_data_style_start']}",
                f"{historic[row][0][0:calc.historic_print_width]+" =":<{calc.historic_print_width}} ",
                f"{historic[row][1][0:calc.historic_print_width]:>{calc.historic_print_width}}",
                f"{cursor['style_finish']}", sep="", end="", flush=True)

def result_data_print(calc_result):
    if type(calc_result) == float:
        print(
            f"{cursor_line(5, calc.padding_left+2)}{cursor['results_data_style_start']}",
            f"{calc_result:{calc.width-3},}".replace(","," ").replace(".",","),
            f"{cursor['style_finish']}", sep="", end="", flush=True)
    else:
        print(
            f"{cursor_line(5, calc.padding_left+2)}{cursor['results_data_style_start']}",
            f"{str(calc_result):>{calc.width-3}}{cursor['style_finish']}",
            sep="", end="", flush=True)

def calc_input_data_print(last_input):
    print(
        f"{cursor_line(9, calc.padding_left+3)}{cursor['dim_start']}",
        f"{last_input[:calc.width-6]:>{calc.width-4}}",
        f" {"=" if last_input != "" else " "}{cursor['style_finish']}",

        sep="", end="", flush=True)
    return input(f"{cursor_line(10,calc.padding_left+4)}\033[8n").lower()