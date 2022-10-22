# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)
# Your program should be uploaded to github before 11:59 pm

# REFERENCE IN 2D PLOT

# print("*******  *******  ****")
# print("*     *  *        *   *")
# print("*        *        *    *")
# print("*        *****    *     *")
# print("*     *  *        *    *")
# print("*     *  *        *   *")
# print("*******  *******  ****")

displayName = "CED"
print_C = [[" " for int_col in range(7)] for int_row in  range(7)]
print_E = [[" " for int_col in range(7)] for int_row in  range(7)]
print_D = [[" " for int_col in range(7)] for int_row in  range(7)]

for row in range(7):
    for col in range(7):
        if ((col == 0 and row != 0) or (row == 0 or row == 6) or (col == 6 and (row != 2 and row !=3))):
            print_C[row][col] = "*" #layout for alpha C
    for col in range(7):
        if (col == 0 or (row == 0 or row == 6) or ((row == 3 and col != 5 and col != 6))):
            print_E[row][col] = "*" #layout for alpha E
    for col in range(7):
        if (col == 0 or (row == 0 or row == 6) and (col < 4) or (col == 4 and (row == 1 or row == 5)) or (col == 5 and (row >= 2 and row < 5))):
            print_D[row][col] = "*" #layout for alpha D

for int_col in range (7):
    for int_row in range(7):
        print(print_C[int_col][int_row], end = " ")
    print(end = "  ")
    for int_row in range(7):
        print(print_E[int_col][int_row], end = " ")
    print(end = "  ")
    for int_row in range(7):
        print(print_D[int_col][int_row], end = " ")
    print()