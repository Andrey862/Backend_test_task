from telegram import ForceReply, Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)
#from .models import TelegramData
from typing import Iterable


def _echo(update, _) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


class BotsPool:
    """
    Handels list of telegram bots
    """

    def __init__(self) -> None:
        self.bots = {}

    def up_bots(self, telegram_data: Iterable):
        for data in telegram_data:
            self.start_bot(bot_id=data.id, token=data.token)

    def start_bot(self, bot_id: int, token: str) -> None:
        # if bots already exists we can to do something with it
        if (bot_id in self.bots):
            # if it is not running we need to start it. otherwise we can just leave
            if (not self.bots[bot_id].running):
                self.bots[bot_id].start_polling()
            return
        # if bot does not exist we need to create one
        self.bots[bot_id] = Updater(token=token)
        self.bots[bot_id].dispatcher.add_handler(
            MessageHandler(Filters.text, _echo))
        self.bots[bot_id].start_polling()

    def stop_bot(self, bot_id: int):
        if (bot_id in self.bots):
            self.bots[bot_id].stop()

    def delete_bot(self, bot_id: int):
        if (bot_id in self.bots):
            self.bots[bot_id].stop()
            del self.bots[bot_id]


bots = BotsPool()
