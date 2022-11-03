import random
import telebot
from telebot import types
from config import token as BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


SET_CANDIES = 133
MAX_CANDIES = 28

USER_NAME = None
CURRENT_CANDIES = SET_CANDIES
USER_CANDIES = None
MOVE_MAKER = None


@bot.message_handler(commands=["start"])
def start(message):
    global USER_NAME
    USER_NAME = message.from_user.first_name
    
    video = open("video.mp4", "rb")
    bot.send_video(message.chat.id, video)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Yes")
    btn2 = types.KeyboardButton("NO")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id,text=f"{USER_NAME}, " +
            "Do You Wanna Play a Game ? YES or NO ",reply_markup=markup)  
    
    bot.register_next_step_handler(message, chek_ready)



def chek_ready(message):
    global USER_NAME , SET_CANDIES
    if message.text == "NO" or message.text == "no" or message.text == "No":
        okay = open("okay.png", "rb")
        bot.send_photo(message.chat.id, okay)
        bot.send_message(message.chat.id, '/start')

    else:
        bot.send_message(message.chat.id,
                f"# На столе лежит {SET_CANDIES} конфета.\n"+ 
                "# Играют два игрока делая ход друг после друга.\n"+
                "# За один ход можно забрать не более чем 28 конфет.\n"+
                "# Все конфеты достаются сделавшему последний ход.")

        msg = bot.send_message(message.chat.id, f"Первый ход за вами, {USER_NAME}")
        bot.register_next_step_handler(msg, check_step)



##------------------------------------------------------------------------------------------##



@bot.message_handler(func=lambda message: message.text == "Yes" or "YES" or "yes")
def repeat(message):
    global CURRENT_CANDIES

    CURRENT_CANDIES = SET_CANDIES
    player_move(message)



def check_step(message):
    global MAX_CANDIES , USER_NAME , CURRENT_CANDIES
    msg_error = "" 

    if message.text.isnumeric():
        candies_taken = int(message.text)
     
        if candies_taken <= 0:
            msg_error = f"{USER_NAME} , количество взятых конфет НЕ может быть 0!"
        if candies_taken > MAX_CANDIES:
            msg_error =  f"{USER_NAME} , можно брать не более {MAX_CANDIES} конфет!"
        if candies_taken > CURRENT_CANDIES: 
            msg_error = (f"{USER_NAME} , конфет осталось {CURRENT_CANDIES}!" 
                    + "\nНельзя взять больше чем есть!")

        if  msg_error:
            m_sent = bot.send_message(message.chat.id, msg_error)
            bot.register_next_step_handler(m_sent, check_step)
        else: 
            CURRENT_CANDIES -= candies_taken 
            bot.send_message(message.chat.id,  f"{USER_NAME} , Вы взяли конфет {candies_taken}" 
                    +f"\nконфет осталось {CURRENT_CANDIES}")
            bot_move(message) #ход бота
    else:
        msg_error = f'Ошибка ввода! Введите число от 1 до {MAX_CANDIES}'
        m_sent = bot.send_message(message.chat.id, msg_error)
        bot.register_next_step_handler(m_sent, check_step)
   


def bot_move(message):                          # ход бота
    global CURRENT_CANDIES , MAX_CANDIES

    if CURRENT_CANDIES <= 28:
        bot.send_message(message.chat.id, f"Последнюю конфету забирает 'bot_name'!"
                    +"\nВы проиграли!")
        msg = bot.send_message(message.chat.id, f"Для повтора введите любую клавишу...")
        bot.register_next_step_handler(msg, repeat)
    else:
        move = CURRENT_CANDIES % (MAX_CANDIES + 1)
        if move < 1:
            move = random.randint(1, MAX_CANDIES)
        CURRENT_CANDIES -= move
        bot.send_message(message.chat.id, f'"bot_name" забирает {move} конфет,')

        player_move(message)



def player_move(message):                           # ход игрока
    global CURRENT_CANDIES , USER_NAME

    if CURRENT_CANDIES <= 28:
        bot.send_message(message.chat.id, f'{USER_NAME}, забирает последнюю конфету!'
                +f'\nВы выиграли!')
        msg = bot.send_message(message.chat.id, f"Для повтора введите любую клавишу...")

        bot.register_next_step_handler(msg, repeat)
    else:
        msg = bot.send_message(message.chat.id, f'{USER_NAME}, Ваш ход...'+
        f'\nКонфет осталось: {CURRENT_CANDIES}')
        bot.register_next_step_handler(msg, check_step)



bot.infinity_polling()

