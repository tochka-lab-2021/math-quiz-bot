#!/usr/bin/env python3

import random
import telebot
from task import Task
from state import State


# Call on "next" button press
def on_next(user_state):
    task = gen_task()
    user_state.task = task.task
    user_state.answer = task.answer


def detect_response(user_state, text):
    result = False
    if text == user_state.answer:
        result = True

    if result:
        positive_response(user_state)
    else:
        negative_response(user_state)

    return result


def negative_response(user_state):
    user_state.negative_tries += 1
    if user_state.negative_tries >= 2:
        return "Oops + button"
    return "Oops"


def positive_response():
    user_state.negative_tries = 0
    return "OK!"


def gen_task():
    # gen 1st number
    a = random.randrange(1, 9, 1)
    # gen 2nd number
    b = random.randrange(1, 9, 1)

    t = Task()
    t.task = f"{a}x{b}"
    t.answer = f"{a*b}"
    return t


state_storage = {}


def get_user_state(user_id):
    if user_id in state_storage:
        return state_storage[user_id]
    return State()


def save_user_state(user_state):
    state_storage[user_state.user_id] = user_state


# Start Bot
f = open("token.txt", "r")
token = f.read()
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def on_start(message):
    bot.reply_to(message, "Привет! Давай порешаем примеры?")


@bot.message_handler(func=lambda m: True)
def on_all(message):
    user_id = message.from_user.id

    state = get_user_state(user_id)

    if state.task == None:
        # Generate new task, show to user.
        task = gen_task()
        state.task = task
        state.tries = 0
        state.user_id = user_id
        save_user_state(state)
        bot.send_message(message.chat.id, task.task)
    else:
        # Check answer
        if message.text == state.task.answer:
            bot.send_message(message.chat.id, f"И правда, {state.task.task}={message.text}. Ещё пример?")
            state.task = None
            state.tries = 0
            state.user_id = user_id
            save_user_state(state)
        else:

            bot.send_message(message.chat.id, "Это ответ?")




if __name__ == "__main__":
    bot.polling()
