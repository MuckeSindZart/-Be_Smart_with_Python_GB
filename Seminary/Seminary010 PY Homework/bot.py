import telebot
from pytube import YouTube
from config import token as TOKEN
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, f"Бот который качает видео с YoTube."
    +" \nДля скачивания скопируйте в сообщении ссылку на видео..."
    +" \nCсылка для примера ..."
    +f"\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=share&utm_source=EJGixIgBCJiu2KjB4oSJEQ", disable_web_page_preview = True)


@bot.message_handler(func=lambda message: True)
def youtube_dwlder(message):
    yt_object = YouTube(message.text)
    meta_data = get_wath_meta_data(message.text)
    video_name = (yt_object.title).split()
    video_name = video_name[0] + '.mp4'

    if video_name == '.mp4':
        video_name = 'video.mp4'

    yt_object.streams.filter(res='360p').first().download(filename=video_name)

    bot.send_message(message.chat.id, f'Название видео "{yt_object.title}"')

    video_msg = open(video_name, "rb")
    bot.send_video(message.chat.id, video_msg)
    bot.send_message(message.chat.id, meta_data)
    
    msg = bot.send_message(message.chat.id, "Качаем еще? Ссылку...")
    bot.register_next_step_handler(msg, youtube_dwlder)

def get_wath_meta_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    interaction_count  = soup.find("meta", itemprop="interactionCount")["content"]
    date_published = soup.find("meta", itemprop="datePublished")["content"]

    meta_data= f'У видео {interaction_count}, опубликовано {date_published}'
    return(meta_data)





bot.infinity_polling()