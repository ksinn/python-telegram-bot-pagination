# -*- coding: utf-8 -*-
import json
from collections import namedtuple

InlineKeyboardButton = namedtuple('InlineKeyboardButton', ['text', 'callback_data'])


class InlineKeyboardPaginator:
    _keyboard_before = None
    _keyboard = None
    _keyboard_after = None

    first_page_label = '« {}'
    previous_page_label = '‹ {}'
    next_page_label = '{} ›'
    last_page_label = '{} »'
    current_page_label = '·{}·'

    def __init__(self, page_count, current_page=1, data_pattern='{page}'):
        self._keyboard_before = list()
        self._keyboard_after = list()

        if current_page is None or current_page < 1:
            current_page = 1
        if current_page > page_count:
            current_page = page_count
        self.current_page = current_page

        self.page_count = page_count

        self.data_pattern = data_pattern

    def _build(self):
        keyboard_dict = dict()

        if self.page_count == 1:
            self._keyboard = list()
            return

        elif self.page_count <= 5:
            for page in range(1, self.page_count+1):
                keyboard_dict[page] = page

        else:
            keyboard_dict = self._build_for_multi_pages()

        keyboard_dict[self.current_page] = self.current_page_label.format(self.current_page)

        self._keyboard = self._to_button_array(keyboard_dict)

    def _build_for_multi_pages(self):
        if self.current_page <= 3:
            return self._build_start_keyboard()

        elif self.current_page > self.page_count - 3:
            return self._build_finish_keyboard()

        else:
            return self._build_middle_keyboard()

    def _build_start_keyboard(self):
        keyboard_dict = dict()

        for page in range(1, 4):
            keyboard_dict[page] = page

        keyboard_dict[4] = self.next_page_label.format(4)
        keyboard_dict[self.page_count] = self.last_page_label.format(self.page_count)

        return keyboard_dict

    def _build_finish_keyboard(self):
        keyboard_dict = dict()

        keyboard_dict[1] = self.first_page_label.format(1)
        keyboard_dict[self.page_count-3] = self.previous_page_label.format(self.page_count-3)

        for page in range(self.page_count-2, self.page_count+1):
            keyboard_dict[page] = page

        return keyboard_dict

    def _build_middle_keyboard(self):
        keyboard_dict = dict()

        keyboard_dict[1] = self.first_page_label.format(1)
        keyboard_dict[self.current_page-1] = self.previous_page_label.format(self.current_page-1)
        keyboard_dict[self.current_page] = self.current_page
        keyboard_dict[self.current_page+1] = self.next_page_label.format(self.current_page+1)
        keyboard_dict[self.page_count] = self.last_page_label.format(self.page_count)

        return keyboard_dict

    def _to_button_array(self, keyboard_dict):
        keyboard = list()

        keys = list(keyboard_dict.keys())
        keys.sort()

        for key in keys:
            keyboard.append(
                InlineKeyboardButton(
                    text=str(keyboard_dict[key]),
                    callback_data=self.data_pattern.format(page=key)
                )
            )
        return _buttons_to_dict(keyboard)

    @property
    def keyboard(self):
        if self._keyboard is None:
            self._build()

        return self._keyboard

    @property
    def markup(self):
        """InlineKeyboardMarkup"""
        keyboards = list(filter(
            bool,
            [
                *self._keyboard_before,
                self.keyboard,
                *self._keyboard_after
            ],
        ))

        if not keyboards:
            return None

        return json.dumps({'inline_keyboard': keyboards})

    def __str__(self):
        if self._keyboard is None:
            self._build()
        return ' '.join(
            [b['text'] for b in self._keyboard]
        )

    def add_before(self, *inline_buttons):
        """
        Add buttons as line above pagination buttons.

        Args:
            inline_buttons (:object:`iterable`): List of object with attributes 'text' and 'callback_data'.

        Returns:
            None
        """
        self._keyboard_before.append(_buttons_to_dict(inline_buttons))

    def add_after(self, *inline_buttons):
        """
        Add buttons as line under pagination buttons.

        Args:
            inline_buttons (:object:`iterable`): List of object with attributes 'text' and 'callback_data'.

        Returns:
            None
        """
        self._keyboard_after.append(_buttons_to_dict(inline_buttons))


def _buttons_to_dict(buttons):
    return [
        {
            'text': button.text,
            'callback_data': button.callback_data,
        }
        for button
        in buttons
    ]
