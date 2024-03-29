import importlib
import os

from logic_application.bot_talk import COMMENT_VARS
from logic_application.telegramapi import Telegram
from command_system import command_list


def load_modules():
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith(".py"), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(chat_id, branch_name, status, action, content=None):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    for c in command_list:
        for k in c.keys:
            if action == k:
                return c.process(branch_name, status, content, chat_id) if content else c.process(branch_name, status, action, chat_id)
    if branch_name in list(COMMENT_VARS.values()):
        content = action
        action = '/save_comment'
    for c in command_list:
        for k in c.keys:
            if action == k:
                return c.process(branch_name, status, content, chat_id) if content else c.process(branch_name, status, action, chat_id)
    return (message, "", [], []), branch_name, status


def _action_detect(action, data_text):
    text = None
    if action.startswith('/'):
        action = action.split(' ')[0]
        text = data_text[len(action):].strip()
    return action, text


def create_answer(data, token, branch_name, status):
    load_modules()
    tg = Telegram(token)
    chat_id = data["chat"]["id"]
    action = data.get("text", '')

    # распознование команд
    action, text = _action_detect(action, action)

    args = get_answer(chat_id, branch_name, status, action, text)
    args, branch_name, status = args[:-2][0], args[-2], args[-1]
    tg.send_message(chat_id, args[0], args[1], args[2], args[3])
    return branch_name, status
