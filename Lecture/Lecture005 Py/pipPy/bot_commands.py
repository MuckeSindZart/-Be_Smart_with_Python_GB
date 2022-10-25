from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log_command(update, context)
    await update.message.reply_text(f'Hallo liebe {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log_command(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log_command(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log_command(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 214
    print(items)
    x = int(items[1])
    y = int(items[2])
    result= x+y
    print(f'{x} + {y} = {result}')
    await update.message.reply_text(f'{x} + {y} = {result}')
