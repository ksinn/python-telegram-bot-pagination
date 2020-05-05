#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram_bot_pagination import InlineKeyboardPaginator

from data import character_pages

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start(update, context):

    paginator = InlineKeyboardPaginator(
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

    paginator = InlineKeyboardPaginator(
        len(character_pages),
        current_page=page,
        data_pattern='character#{page}'
    )

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

