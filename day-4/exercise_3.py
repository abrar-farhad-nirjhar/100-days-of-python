
def print_rows(block):
    for i in block:
        print(f"{i} \n")


row_1 = [' ', ' ', ' ']
row_2 = [' ', ' ', ' ']
row_3 = [' ', ' ', ' ']

block = [row_1, row_2, row_3]

print_rows(block)

placement = list(input(
    "Enter the position where you want to place the block?  "))


placement = list(map(int, placement))

block[placement[1]-1][placement[0]-1] = 'X'

print_rows(block)
