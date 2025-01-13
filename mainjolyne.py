import calculator_display as display
cursor = display.cursor
cursor_line = display.cursor_line

def final_calculation(numbers_set, operators):
    # calculation = numbers_set[0] operators[0] numbers_set[1] operators[1] numbers_set[2]
    if operators[0] == "":
        return numbers_set[0]
    match operators[0]:
        case "+":
            calc_result = float(numbers_set[0]) + float(numbers_set[1])
        case "-":
            calc_result = float(numbers_set[0]) - float(numbers_set[1])
        case "/":
            calc_result = float(numbers_set[0]) / float(numbers_set[1])
        case "*":
            calc_result = float(numbers_set[0]) * float(numbers_set[1])
    if operators[1] == "":
        return str(calc_result)
    match operators[1]:
        case "+":
            calc_result = float(calc_result) + float(numbers_set[2])
        case "-":
            calc_result = float(calc_result) - float(numbers_set[2])
        case "/":
            calc_result = float(calc_result) / float(numbers_set[2])
        case "*":
            calc_result = float(calc_result) * float(numbers_set[2])
    return str(calc_result)

display.setup_print()

calc_result = ""
numbers_set = ["","",""]
operators = ["","",""]
value_number = 0
value_type = 0
while True:
    display.result_print(calc_result)
    calc_line_2 = numbers_set[0] + " " + operators[0] + " " + numbers_set[1] + " " + operators[1] + " " + numbers_set[2]

    while True:
        input_line_3 = str(display.calc_terminal_print(value_number, value_type%2, calc_line_2))

        if value_type%2 == 0:
            if value_number == 0 and calc_result != "" and input_line_3 == "":
                numbers_set[value_number] = str(calc_result)
                display.error_clear_print()
                value_type +=1
                break
            try: input_value = float(input_line_3)
            except Exception:
                display.error_onlynumber_print()
                continue
            numbers_set[value_number] = input_line_3
            display.error_clear_print()
            value_type +=1        
            if value_number == 2:
                calc_result = final_calculation(numbers_set, operators)
                value_type = 0
                value_number = 0
                numbers_set = ["","",""]
                operators = ["","",""]
            break
        elif value_type%2 == 1:
            if input_line_3 in ("+","-","/","*"):
                operators[value_number] = input_line_3
                value_type +=1
                value_number+=1
                break
            elif input_line_3 == "=":
                calc_result = final_calculation(numbers_set, operators)
                value_type = 0
                value_number = 0
                numbers_set = ["","",""]
                operators = ["","",""]
                break
            else:
                display.error_operators_print()
                continue