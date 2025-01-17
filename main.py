import calc_display.calculator_display as data_display
import calc_display.error_display as error_display
import calc_display.set_up_print as set_up_display
from operation_list import configure_input
from launch_operations import calculation, sub_operation_treatment

def main():
    cleared = [["",""],["",""],["",""],["",""]]
    unset = ""
    historic = cleared.copy()
    last_input = unset
    final_result = unset
    set_up_display.clear_print()
    set_up_display.setup_printable_fields()
    try:
        while True:
            calculation_completed = False
            raw_input = data_display.calc_input_data_print(last_input)
            match raw_input:
                case "off":
                    set_up_display.clear_print()
                    exit()
                case "c"|"clear":
                    historic = cleared.copy()
                    last_input = final_result = unset
                    set_up_display.setup_printable_fields()
                    data_display.result_data_print(final_result)
                    data_display.historic_data_print(historic)
                    continue
                case _:
                    set_up_display.setup_printable_fields()
                    data_display.result_data_print(final_result)
                    data_display.historic_data_print(historic)
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
                        error_display.error_message_print(operation_list)
                        continue
                    case _:
                        last_input = " ".join([str(element) for element in operation_list.copy()])
                        sub_operation_treatment(operation_list)
                        final_result = calculation(operation_list)
                        calculation_completed = True
                data_display.result_data_print(final_result)
                error_display.error_message_print(final_result)
                if calculation_completed:
                    error_display.legal_operation_print()
                data_display.historic_data_print(historic)
                historic.insert(0,[last_input,final_result])
                historic.pop(4)
            except Exception:
                last_input = raw_input
                final_result = "error_6_unknown"
                error_display.error_message_print(final_result)
    except KeyboardInterrupt:
        set_up_display.clear_print()
        exit()
main()