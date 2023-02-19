# # Instructions
# # The game is played on a grid that’s 3 squares by 3 squares.
# # Players take turns putting their marks (O or X) in empty squares.
# # The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# # When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

player_win = 1
draw = -1
running = 0
stop = 1

game = running
mark = 'X'
print("Let`s play!" + "\n")
# draw game_board
def display_board():
    # added numbers for squares it helps the user write numbers from 1 to 9
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

# checking if position is empty
def position_check(x):
    if(board[x] == " "):
        return True
    else: # there is no need for the else, you can just replace it with return False
        return False

# checking all board with using
def check_win():
    # using global, because I want to change this variable inside function
    global game
    # Check horizontal
    # do you remember what we explained regardign  the comments? for each comment you can take the corresponding code and extract it to function
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != ' ':
            game = player_win
            return
    # Check vertical
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            game = player_win
    # Check diagonal
    if board[1] == board[5] == board[9] and board[1] != ' ':
        game = player_win
        return
    if board[3] == board[5] == board[7] and board[3] != ' ':
        game = player_win
        return
    if all([x != ' ' for x in board]):
        game = draw
        return
    # game is still running
    game = running

print("Player 1 [X] --- Player 2 [O]\n")

# using while for all functions
def clear_screen():
    print('\n' * 4)

# using while for all functions
while game == running:
    clear_screen()
    display_board()
    if player % 2 != 0:
        print("Player 1's chance")
        mark = 'X'
    else:
        print("Player 2's chance")
        mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if position_check(choice) and choice < 10:
        board[choice] = mark
        player += 1
        check_win()

clear_screen()
display_board()
if game == draw:
    print("Game Draw")
elif game == player_win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Won")
    else:
        print("Player 2 Won")
