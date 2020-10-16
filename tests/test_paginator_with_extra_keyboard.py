# -*- coding: utf-8 -*-

import json
from telegram_bot_pagination import InlineKeyboardPaginator, InlineKeyboardButton
from .data import *

extra_buttons = [
    InlineKeyboardButton('Test1', '1'),
    InlineKeyboardButton('Test2', '2'),
]


def _verify_extra_buttons(line):
    assert line[0]['text'] == 'Test1', \
        'Extra button 1 label not correct'

    assert line[1]['text'] == 'Test2', \
        'Extra button 2 label not correct'

    assert line[0]['callback_data'] == '1', \
        'Extra button 1 data not correct'

    assert line[1]['callback_data'] == '2', \
        'Extra button 2 data not correct'


def test_json_markup_with_before():
    for args, labels in label_test_cases.items():
        paginator = InlineKeyboardPaginator(*args)
        paginator.add_before(
            *extra_buttons
        )
        keyboard = json.loads(paginator.markup, encoding='utf-8')['inline_keyboard']

        _verify_extra_buttons(keyboard[0])

        if not labels:
            continue

        assert len(keyboard[1]) == len(labels), \
            'In case init args {} button count not correct. Mast be {}'.format(args, len(labels))

        for button, label in zip(keyboard[1], labels):
            assert button['text'] == label, \
                'In case init args {} button label not correct. Must be {}'.format(args, label)


def test_json_markup_with_after():
    for args, labels in label_test_cases.items():
        paginator = InlineKeyboardPaginator(*args)
        paginator.add_after(
            *extra_buttons
        )
        keyboard = json.loads(paginator.markup, encoding='utf-8')['inline_keyboard']

        if not labels:
            _verify_extra_buttons(keyboard[0])
            continue

        assert len(keyboard[0]) == len(labels), \
            'In case init args {} button count not correct. Mast be {}'.format(args, len(labels))

        for button, label in zip(keyboard[0], labels):
            assert button['text'] == label, \
                'In case init args {} button label not correct. Must be {}'.format(args, label)

        _verify_extra_buttons(keyboard[1])


def test_json_markup_with_before_after():
    for args, labels in label_test_cases.items():
        paginator = InlineKeyboardPaginator(*args)
        paginator.add_before(
            *extra_buttons
        )
        paginator.add_after(
            *extra_buttons
        )
        keyboard = json.loads(paginator.markup, encoding='utf-8')['inline_keyboard']

        _verify_extra_buttons(keyboard[0])

        if not labels:
            _verify_extra_buttons(keyboard[1])
            continue

        assert len(keyboard[1]) == len(labels), \
            'In case init args {} button count not correct. Mast be {}'.format(args, len(labels))

        for button, label in zip(keyboard[1], labels):
            assert button['text'] == label, \
                'In case init args {} button label not correct. Must be {}'.format(args, label)

        _verify_extra_buttons(keyboard[2])


def test_one_page_keyboard_json_markup_with_before():
    for test_case in one_page_test_cases:
        paginator = InlineKeyboardPaginator(*test_case)
        paginator.add_before(
            *extra_buttons
        )
        keyboard = json.loads(paginator.markup)['inline_keyboard']

        _verify_extra_buttons(keyboard[0])


def test_one_page_keyboard_json_markup_with_after():
    for test_case in one_page_test_cases:
        paginator = InlineKeyboardPaginator(*test_case)
        paginator.add_after(
            *extra_buttons
        )
        keyboard = json.loads(paginator.markup)['inline_keyboard']

        _verify_extra_buttons(keyboard[0])


def test_one_page_keyboard_json_markup_with_before_and_after():
    for test_case in one_page_test_cases:
        paginator = InlineKeyboardPaginator(*test_case)
        paginator.add_before(
            *extra_buttons
        )
        paginator.add_after(
            *extra_buttons
        )
        keyboard = json.loads(paginator.markup)['inline_keyboard']

        _verify_extra_buttons(keyboard[0])
        _verify_extra_buttons(keyboard[1])
