    # python-telegram-bot-pagination

[![Download Month](https://img.shields.io/pypi/v/python-telegram-bot-pagination.svg)](https://pypi.python.org/pypi/python-telegram-bot-pagination)
[![Build Status](https://travis-ci.com/ksinn/python-telegram-bot-pagination.svg?branch=master)](https://travis-ci.com/ksinn/python-telegram-bot-pagination)

Provide easy way for create number pagination with inline keyboard for telegram bot on python.

**InlineKeyboardPaginator**

[Example](https://github.com/ksinn/python-telegram-bot-pagination/blob/master/examples/example.py) with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

[Example](https://github.com/ksinn/python-telegram-bot-pagination/blob/master/examples/example2.py) with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/ex1.png)  ![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/f1.jpg)

**InlineKeyboardSimplePaginator**

This paginator can be used similarly to InlineKeyboardPaginator. 

It is suitable when page numbers are not as important to us as the ability to quickly view them and scroll around page
(e.g. when you click the next page button on the last one, the first page will open).

[Example](https://github.com/ksinn/python-telegram-bot-pagination/blob/master/examples/example3.py) with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/simple_2.png)  ![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/simple_1.png)

---
* [Installation.](#installation)
* [Usage.](#usage)
* [Button render controlling.](#button-render-controlling)
* [Adding extra button.](#adding-extra-button)

#### Installation

    pip install python-telegram-bot-pagination

#### Usage

```python3
from telegram_bot_pagination import InlineKeyboardPaginator, InlineKeyboardSimplePaginator

paginator = InlineKeyboardPaginator(
    page_count,
    current_page=page,
    data_pattern='page#{page}'
)

# you can use two types of Pagianators in a similar way
simple_paginator = InlineKeyboardSimplePaginator(
    page_count,
    current_page=page,
    data_pattern='page#{page}'
)
```
```python3
bot.send_message(
    chat_id,
    text,
    reply_markup=paginator.markup,
)
```

Init arguments:
* page_count - integer, total 1-based pages count.
* current_page - integer, 1-based current page. Default 1
* data_pattern - string with python style formatting named argument 'page'. Used for generate callback data for button. Default '{page}'

Properties:
* markup - json object for [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) TelegramAPI type
* keyboard - array of button's dist 

#### Button render controlling
For edit button render, use paginator object properties:

| InlineKeyboardPaginator | InlineKeyboardSimplePaginator |
|-------------------------|-------------------------------|
| previous_page_label     | previous_page_label           |
| current_page_label      | current_page_label            |
 | next_page_label         | next_page_label               |
 | first_page_label        | -                             |
 | last_page_label         | -                             |


All of them can by python style formatting string with one arg, or simple string.

For example:
```python3
class MyPaginator(InlineKeyboardPaginator):
    first_page_label = '<<'
    previous_page_label = '<'
    current_page_label = '-{}-'
    next_page_label = '>'
    last_page_label = '>>'

paginator = MyPaginator(page_count)
```
```python3
class MyPaginator(InlineKeyboardSimplePaginator):
    previous_page_label = '<'
    current_page_label = '{}-{}'
    next_page_label = '>'

paginator = MyPaginator(page_count)
```
Results:

InlineKeyboardPaginator

![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/m2.jpg)

InlineKeyboardSimplePaginator

![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/simple_3.png)

#### Adding extra button
For adding button line before and after pagination use methods:

* add_before(*args)
* add_after(*args)

Each argument mast provide property 'text' and 'callback_data'

For example:
```python3
paginator.add_before(
    InlineKeyboardButton('Like', callback_data='like#{}'.format(page)),
    InlineKeyboardButton('Dislike', callback_data='dislike#{}'.format(page))
)
paginator.add_after(InlineKeyboardButton('Go back', callback_data='back'))

```

Result:

![](https://github.com/ksinn/python-telegram-bot-pagination/raw/master/examples/media/ex1.png)

