import calculator_display as display
cursor = display.cursor
cursor_line = display.cursor_line
from operation_list import configure_input, add_first_operand, update_operation
from launch_operations import calculation, sub_operation_treatment

def main():
    cleared = [["",""],["",""],["",""],["",""]]
    historic = cleared.copy()
    last_input = ""
    display.clear_print()
    display.setup_printable_fields()

    while True:
        raw_input = display.calc_input_data_print(last_input)
        match raw_input:
            case "off":
                display.clear_print()
                exit()

        display.setup_printable_fields()
        display.historic_data_print(historic)
        try:
            operation_list = configure_input(raw_input)
            match operation_list:
                case "error_4_incorrectnumeral":
                    raise Exception(display.error_message_print("error_4_incorrectnumeral"))
                case "error_2_multipleoperators":
                    raise Exception(display.error_message_print("error_2_multipleoperators"))
                case "error_5_illegalentry":
                    raise Exception(display.error_message_print("error_5_illegalentry"))
                case "error_3_blankinput":
                    raise Exception(display.error_message_print("error_3_blankinput"))
                case _:
                    last_input = " ".join([str(element) for element in operation_list.copy()])
                    sub_operation_treatment(operation_list)
                    final_result = calculation(operation_list)
                    display.error_message_print(final_result)
                    display.result_data_print(final_result)
                    historic.insert(0,[last_input,final_result])
                    historic.pop(4)
        except Exception as message:
            # message = display.error_message_print("error_3_blankinput")
            last_input = ""
main()