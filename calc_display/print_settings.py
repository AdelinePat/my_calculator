"""
print settings to generate calculator interface with special
characters and ansi escape sequencies
"""
padding_left = 20
padding_top = 1
width = 28
historic_width = 33
historic_print_width = historic_width//2-2

box = {
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
    "happy_message_style_start" : "\033[0;6;1;38;5;201m",

    "style_finish" : "\033[0m"
    # "color_end" : "\033[39m",
    # "red_start" : "\033[31m",
}
def cursor_line(y,x=0):
    coordinate = "\033[" + str(y+ padding_top) + ";" + str(x) + "H"
    return coordinate