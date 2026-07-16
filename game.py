board = ['','','','','','','','','']
def print_board():
    print(f" {board[0]}  | {board[1]}  | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]}  | {board[4]}  | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]}  | {board[7]}  | {board[8]} ") 
print_board()
for turrn in range(9):
    move = int(input("choose a spot (0-8): "))
    board[move] = 'X'
    print_board()
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print_board()
        print ("X wins!")
        break