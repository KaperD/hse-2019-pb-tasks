#!/usr/bin/env python3
import sys
import traceback
from alarm_user_handler import AlarmUserHandler
from bot import UserIndependentBot
from tictactoe_user_handler import TicTacToeUserHandler
import telebot

bot = telebot.TeleBot('1036507101:AAEuq0Da7fVQ88U7J7b3QBsFEU85jj_MZMw')


def send_message(to_user_id: int, message: str) -> None:
    bot.send_message(to_user_id, message)


bbot = UserIndependentBot(send_message=send_message, user_handler=TicTacToeUserHandler)


@bot.message_handler(content_types=['text'])
def main(message) -> None:
    try:
        bbot.handle_message(message.from_user.id, message.text)
    except Exception:  # pylint: disable=W0703
        traceback.print_exc()


bot.polling(none_stop=True, interval=0)
