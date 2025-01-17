import calc_display.print_settings as calc
from calc_display.print_settings import cursor_line, cursor
'''
    clear entire terminal from position 0,0
'''
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

        f"{cursor_line(1)}{" ":^{calc.padding_left}}{calc.box['angle_tl']}",
        f"{"":{calc.box['horizontal']}^{calc.width}}{calc.box['vertical_bis_v']}",
        f"{"":{calc.box['horizontal']}^{calc.historic_width}}{calc.box['angle_tr']}",
        f"{cursor['light_line_clear']}",

        f"{cursor_line(2)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",

        f"{cursor_line(3)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{cursor['result_message_style_start']}{" Résultat :":<{calc.width}}",
        f"{cursor['calc_box_style_start']}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(4)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{cursor['dim_start']}{"":{calc.box['horizontal']}^{calc.historic_width}}",
        f"{cursor['bold_dim_end']}{cursor['bold_start']}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(5)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(6)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(7)}{" ":^{calc.padding_left}}{calc.box['horizontal_bis_>']}",
        f"{"":{calc.box['horizontal_bis']}^{calc.width}}{calc.box['vertical_bis_<']}",
        f"{cursor['dim_start']}{"":{calc.box['horizontal']}^{calc.historic_width}}",
        f"{cursor['bold_dim_end']}{cursor['bold_start']}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(8)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(9)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(10)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{cursor['dim_start']}{"":{calc.box['horizontal']}^{calc.historic_width}}",
        f"{cursor['bold_dim_end']}{cursor['bold_start']}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(11)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(12)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{cursor['instructions_style_start']}{"Entrez votre calcul":^{calc.width}}",
        f"{cursor['calc_box_style_start']}{calc.box['vertical_bis']}",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(13)}{" ":^{calc.padding_left}}{calc.box['vertical_>']}",
        f"{"":{calc.box['horizontal']}^{calc.width}}{calc.box['vertical_bis_^']}",
        f"{"":{calc.box['horizontal']}^{calc.historic_width}}{calc.box['vertical_<']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(14)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}} ",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(15)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}} ",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(16)}{" ":^{calc.padding_left}}{calc.box['vertical']}",
        f"{" ":^{calc.width}} ",
        f"{" ":^{calc.historic_width}}{calc.box['vertical']}",
        f"{cursor['light_line_clear']}",
        
        f"{cursor_line(17)}{" ":^{calc.padding_left}}{calc.box['angle_bl']}",
        f"{"":{calc.box['horizontal']}^{calc.width}}{calc.box['horizontal']}",
        f"{"":{calc.box['horizontal']}^{calc.historic_width}}{calc.box['angle_br']}",
        f"{cursor['light_clear']}",

        f"{cursor['style_finish']}", sep="", end="", flush=True
        )