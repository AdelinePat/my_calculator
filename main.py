import calculator_display as display
cursor = display.cursor
cursor_line = display.cursor_line
from input import input_user
from calculation import add_first_operand, update_operation, calculation, sub_operation_treatment

def main():
    while True:
        display.clear_print()
        display.setup_print()
        clean_input = input_user(display.calc_terminal_print())
        display.calc_terminal_print(clean_input)
        sub_operation_treatment(clean_input)
        final_result = calculation(clean_input)
        display.result_print(final_result)
    


    # print(f"résultat final : {final_result}")
main()