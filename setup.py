from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-telegram-bot-pagination1',
    version='0.0.1',
    packages=['telegram_bot_pagination'],
    url='https://github.com/ksinn/pyTelegramBotPagination',
    license='GPL2',
    author='ksinn',
    author_email='ksinnd@gmail.com',
    description='Python inline keyboard pagination for Telegram Bot API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='telegram bot api pagination keyboard inline tools',
)
