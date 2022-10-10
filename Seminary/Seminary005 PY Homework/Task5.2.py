import random

board = [[' ', ' ', ' '],  # - пустое поле, 1 - крестик, 2 - нолик
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


# крестики ставит игрок, нолики - компьютер

def draw_board():
    print(' ', '  1,   2,   3 ')
    print(1, board[0])
    print(2, board[1])
    print(3, board[2])


def player_move():
    print('\nВведите координаты через пробел: ')
    move = [0, 0]
    move = list(map(int, input().split(' ')))

    if board[move[0]-1][move[1]-1] != ' ':
        print('Занято')
        player_move()
    else:
        board[move[0]-1][move[1]-1] = 'X'

    if win_chek():
        print("---------------")
        print("Player победил!")
        exit()


def bot_move():
    move = [0, 0]
    move[0] = random.randint(0, 2)
    move[1] = random.randint(0, 2)
    if board[move[0]][move[1]] != ' ':
        bot_move()
    else:
        board[move[0]][move[1]] = 'O'
    print(f'\nBot ходит {move[0]+1} {move[1]+1} ')

    if win_chek():
        print("-----------")
        print("Bot победил!")
        exit()


def win_chek():
    if (board[0][0] == board[0][1] == board[0][2]) and board[0][2] != ' ' or (
            board[1][0] == board[1][1] == board[1][2]) and board[1][2] != ' ' or (
            board[2][0] == board[2][1] == board[2][2]) and board[2][2] != ' ' or (
            board[0][0] == board[1][0] == board[2][0]) and board[2][0] != ' ' or (
            board[0][1] == board[1][1] == board[2][1]) and board[2][1] != ' ' or (
            board[0][2] == board[1][2] == board[2][2]) and board[2][2] != ' ' or (
            board[0][0] == board[1][1] == board[2][2]) and board[2][2] != ' ' or (
            board[2][0] == board[1][1] == board[0][2]) and board[0][2] != ' ':
        return True
    else:
        return False


##---------------------------------------------------------------##
print("Крестики-нолики.")
draw_board()
print("\nДля того, чтобы поставить крестик нужно указать номер строки и номер столбца")


for i in range(9):
    player_move()
    draw_board()
    bot_move()
    draw_board()

print("Ничья.")
exit()
