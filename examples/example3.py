#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

from telegram import InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram_bot_pagination import InlineKeyboardSimplePaginator

from data import character_pages

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start(update, context):

    paginator = InlineKeyboardSimplePaginator(
        len(character_pages),
        data_pattern='character#{page}'
    )

    update.message.reply_text(
        text=character_pages[0],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


def characters_page_callback(update, context):
    query = update.callback_query

    query.answer()

    page = int(query.data.split('#')[1])

    paginator = InlineKeyboardSimplePaginator(
        len(character_pages),
        current_page=page,
        data_pattern='character#{page}'
    )

    paginator.add_before(
        InlineKeyboardButton('Like', callback_data='like#{}'.format(page)),
        InlineKeyboardButton('Dislike', callback_data='dislike#{}'.format(page))
    )
    paginator.add_after(InlineKeyboardButton('Go back', callback_data='back'))

    query.edit_message_text(
        text=character_pages[page - 1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(characters_page_callback, pattern='^character#'))

updater.start_polling()
updater.idle()

