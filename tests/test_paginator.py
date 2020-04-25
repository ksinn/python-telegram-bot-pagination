# -*- coding: utf-8 -*-

from telegram_bot_pagination import InlineKeyboardPaginator
from .data import *


def test_button_label():
    for args, labels in label_test_cases.items():
        paginator = InlineKeyboardPaginator(*args)
        keyboard = paginator.keyboard

        assert len(keyboard) == len(labels), \
            'In case init args {} button count not correct. Mast be {}'.format(args, len(labels))

        for button, label in zip(keyboard, labels):
            assert button['text'] == label, \
                'In case init args {} button label not correct. Must be {}'.format(args, label)


def test_one_page_keyboard():
    for test_case in one_page_test_cases:
        paginator = InlineKeyboardPaginator(*test_case)
        assert paginator.markup is None, \
            'In case init args {} markup mast be None'.format(test_case)


def test_callback_data():
    for page_count in range(2, 6):
        for current_page in range(2, 6):
            paginator = InlineKeyboardPaginator(page_count, current_page, data_pattern='test#{page}#')
            keyboard = paginator.keyboard
            for button, num in zip(keyboard, range(1, 6)):
                data = 'test#{}#'.format(num)
                assert button['callback_data'] == data, \
                    'In case init args {} callback_data mast be {}'.format((page_count, current_page, 'test#{page}#'), data)

    for args, output in data_test_case.items():
        paginator = InlineKeyboardPaginator(*args)
        keyboard = paginator.keyboard
        for button, data in zip(keyboard, output):
            assert button['callback_data'] == data, \
                    'In case init args {} callback_data mast be {}'.format(args, data)


def test_json_markup():
    for args, markup in markup_test_cases.items():
        paginator = InlineKeyboardPaginator(*args)
        assert paginator.markup == markup, \
                'In case init args {} markup not correct'.format(args)





