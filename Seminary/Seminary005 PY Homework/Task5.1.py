# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#       a) Добавьте игру против бота

from random import randint


def main_game_body():
    players = mode()
    turn = t(players)

    value_candies = 2021  # количество конфет для игры

    while value_candies > 28:

        if turn:
            value_candies -= candies_move(value_candies,
                                          players[0], players[2])
            turn = False

        else:
            value_candies -= candies_move(value_candies,
                                          players[1], players[3])
            turn = True
    end_game(value_candies, players, turn)


def mode():
    try:
        game_type = int(input(
            f"Режим игры: \t1 - два игрокa\n\t\t2 - игра с ботом\n\t\t3 -> ботVSбот\n"))
    except ValueError:
        print("Это не то! Вводить надо целые числа от 1 или 2! Ну или 3..")

    if game_type == 1:
        print('Режим - два игрокa')
        game_mode = ['', '', False, False]
        game_mode[0] = 'Player_1'
        game_mode[1] = 'Player_2'

    elif game_type == 2:
        print('Режим - игра с ботом')
        game_mode = ['', '', False, True]
        game_mode[0] = 'Player_1'
        game_mode[1] = 'Bot_1'

    else:
        print('Режим - бота с ботом')
        game_mode = ['', '', True, True]
        game_mode[0] = 'Bot_1'
        game_mode[1] = 'Bot_2'

    return game_mode


def t(players):
    turn = randint(0, 1)

    if turn:
        print(f"Первым ходит: {players[0]}")
    else:
        print(f"Первым ходит: {players[1]}")
    return turn


def candies_move(value_candies, player_name, check_bot):
    print(f"На столе осталось: {value_candies} конфет")

    if check_bot == False:  # Шаг игрока
        try:
            move = int(input(f"{player_name}, сколько конфет возьмете? "))
            while move < 1 or move > 28:
                move = int(input("По правилам, от 1 до 28: "))
        except ValueError:
            print("Это не то! Вводить надо целые числа от 1 до 28!")
    else:   # Шаг бота
        move = bot_candies_move(value_candies, player_name)
    return move


def bot_candies_move(value_candies, player_name):

    if value_candies > 100:     # Интрига до конца
        move = randint(1, 28)  
    elif value_candies <= 28:
        move = value_candies
    else:
        move = value_candies % (29)

    if move == 0:
        move = 1
    print(f"{player_name}, берет {move} конфет")

    return move


def end_game(value_candies, players, turn):
    if turn:
        winer = players[0]
    else:
        winer = players[1]

    print(f'\nНа столе осталось {value_candies}шт. их забирает {winer}')
    print('-----------------------------------------')
    print(f'{winer} выиграл!')
    exit()


##---------------------------------------------------------------##
print("# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n\
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n\
# Все конфеты оппонента достаются сделавшему последний ход.")
main_game_body()
