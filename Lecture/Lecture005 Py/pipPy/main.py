##ex001-------------------------------------------------##

""" 
from isOdd import isOdd

print(isOdd(1))
print(isOdd(4)) 
"""

##ex002-------------------------------------------------##

""" 
from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    # Do some work
    bar.next()
bar.finish() 
"""

##ex003-------------------------------------------------##

""" 
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
#Python is 👍
print(emoji.emojize('Python is :thumbsup:', language='alias'))
#Python is 👍
print(emoji.demojize('Python is 👍'))
#Python is :thumbs_up:
print(emoji.emojize("Python is fun :red_heart:"))
#Python is fun ❤
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#Python is fun ❤️ #red heart, not black heart
print(emoji.is_emoji("👍"))
True """

##ex004-------------------------------------------------##
""" 
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

# make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
 """
##ex005-------------------------------------------------##

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5767655379:AAHv9qumtFLr4xfBxAew2gQqNPiNa2gbe1E").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


print('say hello')
app.run_polling()

##ex006-------------------------------------------------##
