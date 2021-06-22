from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from data import character_pages



bot = Bot(token='BOT-TOKEN')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nI'm aiogram paginator example!\n /text")

    
@dp.message_handler(commands=['text'])
async def get_log_command(message: types.Message):
    await send_character_page(message)
    send_character_page(call.message)

    
@dp.callback_query_handler(func=lambda call: call.data.split('#')[0]=='character')
async def characters_page_callback(call):
    page = int(call.data.split('#')[1])
    bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    send_character_page(call.message, page, edit=True)



async def send_character_page(message: Message, page: int = 1, edit: bool = False):
    paginator = Paginator(
        len(character_pages),
        current_page=page,
        data_pattern='character#{page}')
    if edit:
        try:
            await bot.edit_message_text(character_pages[page - 1],
                                        message.chat.id, message.message_id,
                                        reply_markup=paginator.markup
                                        )
        except Exception as e:
           pass
    else:
        await bot.send_message(
            message.chat.id,
            character_pages[page - 1],
            reply_markup=paginator.markup,
            parse_mode='Markdown'
        )


if __name__ == '__main__':
    executor.start_polling(dp)
