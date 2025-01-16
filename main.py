import calculator_display as display
cursor = display.cursor
cursor_line = display.cursor_line
from operation_list import configure_input, add_first_operand, update_operation
from launch_operations import calculation, sub_operation_treatment

def main():
    historic = [["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
    last_input = "                                          "
    display.clear_print()
    display.setup_printable_fields()

    while True and last_input != "off" :
        operation_list = configure_input(display.calc_input_data_print(last_input))
        if operation_list == "off":
            last_input = "off"
            display.clear_print()
            pass
        else:
            last_input = " ".join([str(element) for element in operation_list.copy()])
            sub_operation_treatment(operation_list)
            final_result = calculation(operation_list)
            display.setup_printable_fields()
            match final_result:
                case "error_1st_operant":
                    display.error_1_first_operator_print()
                case _:
                    display.error_clear_print
            display.result_data_print(final_result)
            display.historic_data_print(historic)
            historic.insert(0,[last_input,final_result])
            historic.pop(10)
main()