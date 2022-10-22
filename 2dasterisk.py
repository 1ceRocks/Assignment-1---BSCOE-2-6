# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)
# Your program should be uploaded to github before 11:59 pm

# REFERENCE IN 2D PLOT

# print("*****  *****  ****")
# print("*      *      *   *")
# print("*      *****  *   *")
# print("*      *      *   *")
# print("*****  *****  ****")

displayName = "CED"
print_C = [[" " for int_col in range(5)] for int_row in  range(5)]
print_E = [[" " for int_col in range(5)] for int_row in  range(5)]
print_D = [[" " for int_col in range(5)] for int_row in  range(5)]

#code for C
for row in range(5):
    for col in range(5):
        if (col == 0 or (row == 0 or row == 4) and (col > 0)):
            print_C[row][col] = "*"

#code for E
for row in range(5):
    for col in range(5):
        if (col == 0 or (row == 0 or row == 2 or row == 4) and (col > 0)):
            print_E[row][col] = "*"

#code for D
for row in range(5):
    for col in range(5):
        if (col == 0 or (col == 4 and (row != 0 and row != 4)) or ((row == 0 or row == 4) and (col > 0 and col < 4))):
            print_D[row][col] = "*"

for int_col in range (5):
    for int_row in range(5):
        print(print_C[int_col][int_row], end = "")
    print(end = "  ")
    for int_row in range(5):
        print(print_E[int_col][int_row], end = "")
    print(end = "  ")
    for int_row in range(5):
        print(print_D[int_col][int_row], end = "")
    print()