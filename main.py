import calculator_display as display
cursor = display.cursor
cursor_line = display.cursor_line
from input import input_user
from calculation import add_first_operand, update_operation, calculation, sub_operation_treatment

def main():
    historic = [["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
    last_input = ""
    display.clear_print()
    display.setup_print()
    while True:
        clean_input = input_user(display.calc_terminal_print(last_input))
        last_input = " ".join([str(element) for element in clean_input.copy()])
        sub_operation_treatment(clean_input)
        final_result = calculation(clean_input)
        display.setup_print()
        display.result_print(final_result)
        historic.insert(0,[last_input,final_result])
        historic.pop(10)
main()