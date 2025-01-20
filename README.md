# 🖩 calculator 
<!-- # ✖️➗➕➖🟰 Calculator -->
Group project : create a calculator inside console

## 📝 Instruction 
1. User inputs their operation for integer or floats freely
2. Simple operators are allowed : + - / *
3. The algorithm is able to calculate the user's operation and return the result
4. Management of errors (wrong input, impossible operations)...
5. **bonus** : display the history of operation. The user can erase the history if they wish

*the math module and eval() function are forbidden*

## 👥 Group members
- [Jolyne Mangeot](https://github.com/jolyne-mangeot)
- [Eltigani Abdallah](https://github.com/eltigani-abdallah)
- [AdelinePat](https://github.com/AdelinePat)

---

## 🚀 Features
- **input operation at once**:
  - regular expression used for user's input (re library)
  - get a list of number (int and float) and operators, return an error if anything else is written
  - check the start of the list, return an error if it doesn't start with a number, + or -
  - Add 0 if list starts with + or -
- **calculate**:
  - simple operation
  - update operation list by inserting the result inside original list and then remove from list both operand and operator
  - complex operation with parenthesis (create a sublist inside original list in order to calculate inside the sublist first)
  - return ZeroDivisionError when user tries to divide by 0
- **display**:
  - ansi escape sequencies enable user-friendly display inside console
- **operations' record**:
  - The last four operations are saved and displayed using a list
  - Clearing record is possible
- **exit algorithm**:
  - off command let user stop main algorithm without error
  - ctrl+c let user stop main algorithm without error
  
## 📂 Directories and files
- **calc_display** directory : contains all files related to display calculator inside console
- **operations** directory : contains all files related to the treatment of input and actual mathematical operations
  
---




