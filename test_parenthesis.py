print("=========== TEST CALCULETTE ===============")

this_list = ["(","(", 1, "-", 2, ")", 2, "+","(", 3, "-", 4, ")", "-", "(", 5, "-", 6, ")", ")"]
print(this_list)

# while "(" in this_list and ")" in this_list:
#     parenthesis_index = this_list.index("(")
#     this_list.pop(parenthesis_index)
#     print(parenthesis_index)

parenthesis_list = list(enumerate(this_list))
print(parenthesis_list)
start = []
end = []

# print(parenthesis_list[2][1])
# print(len(parenthesis_list))
for index in range(len(this_list)):
    if this_list[index] == "(":
        start.append(index)
        print(start)

for index in range(len(this_list)):
    if this_list[index] == ")":
        end.append(index)
        print(end)

# for index in range(len(parenthesis_list)):
#     if parenthesis_list[index][1] == "(":
#         index_start = parenthesis_list[index][0]
#         start.append(index_start)
#         # print(index_start)
#         print(start)

# for index in range(len(parenthesis_list)):
#     if parenthesis_list[index][1] == ")":
#         index_end = parenthesis_list[index][0]
#         end.append(index_end)
#         # print(index_end)
#         print(end)
# for index in range(len(this_list)):
#     print(start[index][0])

# for index in range(len(this_list+1)):
#     if start[index+1][0] < end[index][0]:
#         range_of_sub_operation = slice(start[index+1], end[index])
#         sub_operation = this_list[range_of_sub_operation]
#         print(sub_operation)

for i in range(len(start)-1):
    if start[i+1] < end[i]:
            range_of_sub_operation = slice(start[i+1], end[i]+1)
            sub_operation = this_list[range_of_sub_operation]
            # this_list.pop(i+1)
            # this_list.pop(i)
            # this_list.pop(i-1)
            # sub_operation.pop(-1)
            # sub_operation.pop(0)

            print(f"sub operation avant for : {sub_operation}")
            
            for index in reversed(range(start[i+1], end[i]+1)):
                this_list.pop(index)

  
            print(f"sub operation apres : {sub_operation}")