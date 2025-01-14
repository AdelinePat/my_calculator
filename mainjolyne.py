import calculator_display_copy as display
cursor = display.cursor
cursor_line = display.cursor_line

def final_calculation(numbers_set, operator):
    if operator == "=":
        return float(numbers_set[0])
    match operator:
        case "+":
            calc_result = float(numbers_set[0]) + float(numbers_set[1])
        case "-":
            calc_result = float(numbers_set[0]) - float(numbers_set[1])
        case "/":
            calc_result = float(numbers_set[0]) / float(numbers_set[1])
        case "*":
            calc_result = float(numbers_set[0]) * float(numbers_set[1])
        case _:
            calc_result = float(numbers_set[0])
    return float(calc_result)

display.clear_print()

calc_result = 0.0
numbers_set = [0.0,0.0]
operator = " "
value_type = 0
first_number_taken = False

while True:
    display.setup_print()
    display.result_print(calc_result)
    value_number = 0
    while True:
        if first_number_taken:
            value_number = 1
        input_line_3 = str(display.calc_terminal_print(numbers_set[0], operator))
        if value_type%2 == 0:
            try: input_value = float(input_line_3)
            except Exception:
                display.error_onlynumber_print()
                continue
            numbers_set[value_number] = input_line_3
            if first_number_taken:
                calc_result = numbers_set[0] = final_calculation(numbers_set, operator)
            first_number_taken = True
            value_type +=1
            display.error_clear_print()
            break
        elif value_type%2 == 1:
            match input_line_3:
                case "+"|"-"|"/"|"*":
                    operator = input_line_3
                    value_type +=1
                    display.error_clear_print()
                    break
                case "":
                    calc_result = numbers_set[0] = final_calculation(numbers_set, operator)
                    break
                case "c":
                    calc_result = 0.0
                    numbers_set = [0.0,0.0]
                    operator = " "
                    value_type = 0
                    first_number_taken = False
                    display.error_operators_print()
                    break
                case _:
                    display.error_operators_print()
                    continue