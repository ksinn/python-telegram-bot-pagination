# -*- coding: utf-8 -*-
import os

from telebot import TeleBot
from telebot.types import InlineKeyboardButton

from telegram_bot_pagination import InlineKeyboardPaginator
from data import character_pages

bot = TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(func=lambda message: True)
def get_character(message):
    send_character_page(message)


@bot.callback_query_handler(func=lambda call: call.data.split('#')[0]=='character')
def characters_page_callback(call):
    page = int(call.data.split('#')[1])
    bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    send_character_page(call.message, page)


def send_character_page(message, page=1):
    paginator = InlineKeyboardPaginator(
        len(character_pages),
        current_page=page,
        data_pattern='character#{page}'
    )

    paginator.add_before(
        InlineKeyboardButton('Like', callback_data='like#{}'.format(page)),
        InlineKeyboardButton('Dislike', callback_data='dislike#{}'.format(page))
    )
    paginator.add_after(InlineKeyboardButton('Go back', callback_data='back'))

    bot.send_message(
        message.chat.id,
        character_pages[page-1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


bot.polling()
