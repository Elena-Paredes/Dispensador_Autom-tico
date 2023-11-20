# TelegramBot.py
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

class TelegramBot:
    def __init__(self, token, chat_id):
        self.bot = Bot(token)
        self.chat_id = chat_id

    def send_message(self, message):
        self.bot.send_message(chat_id=self.chat_id, text=message)

    def cleanup(self):
        # No se requiere limpieza especial para el bot de Telegram
        pass
