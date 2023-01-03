# example use aiogram

import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton

from telegram_bot_pagination import InlineKeyboardPaginator
from data import character_pages

bot = Bot(token="BOT_TOKEN")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


async def send_character_page(msg, page=1):
    bot: Bot = msg.bot
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

    await bot.send_message(
        msg.chat.id,
        character_pages[page-1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )


async def characters_page_callback(query: CallbackQuery):
    bot: Bot = query.bot

    page = int(msg.data.split('#')[1])
    await bot.delete_message(
        query.message.chat.id,
        query.message.message_id
    )
    await send_character_page(query.message, page)


async def get_character(msg: Message):
    await send_character_page(msg)


if __name__ == "__main__":
    
    dp.register_callback_query_handler(characters_page_callback, lambda c: c.data.split('#')[0]=='character')
    dp.register_message_handler(get_character, content_types=['text'])

    executor.start_polling(dp, skip_updates=True)
