import calculator_display as display
from operation_list import configure_input
from launch_operations import calculation, sub_operation_treatment

def main():
    cleared = [["",""],["",""],["",""],["",""]]
    unset = ""
    historic = cleared.copy()
    last_input = unset
    final_result = unset
    display.clear_print()
    display.setup_printable_fields()
    try:
        while True:
            calculation_completed = False
            raw_input = display.calc_input_data_print(last_input)
            match raw_input:
                case "off":
                    display.clear_print()
                    exit()
                case "c"|"clear":
                    historic = cleared.copy()
                    last_input = final_result = unset
                    display.setup_printable_fields()
                    display.result_data_print(final_result)
                    display.historic_data_print(historic)
                    continue
                case _:
                    display.setup_printable_fields()
                    display.result_data_print(final_result)
                    display.historic_data_print(historic)
            try:
                operation_list = configure_input(raw_input)
                match operation_list:
                    case "error_4_incorrectnumeral":
                        last_input = raw_input
                        final_result="error_4_incorrectnumeral"
                    case "error_2_multipleoperators":
                        last_input = raw_input
                        final_result = "error_2_multipleoperators"
                    case "error_5_illegalentry":
                        last_input = raw_input
                        final_result = "error_5_illegalentry"
                    case "error_3_blankinput":
                        display.error_message_print(operation_list)
                        continue
                    case _:
                        last_input = " ".join([str(element) for element in operation_list.copy()])
                        sub_operation_treatment(operation_list)
                        final_result = calculation(operation_list)
                        calculation_completed = True
                display.result_data_print(final_result)
                display.error_message_print(final_result)
                if calculation_completed:
                    display.legal_operation_print()
                display.historic_data_print(historic)
                historic.insert(0,[last_input,final_result])
                historic.pop(4)
            except Exception:
                last_input = raw_input
                final_result = "error_6_unknown"
                display.error_message_print(final_result)
    except KeyboardInterrupt:
        display.clear_print()
        exit()
main()