#!/usr/bin/env python3

import random


def main():
    task = gen_task()
    print(task)


def user_state(user_id):
    return ""


def detect_response(text):
    result = True
    return result


def negative_response():
    return "Oops"


def positive_response():
    return "OK!"


def gen_task():
    # gen 1st number
    a= random.randrange(1, 9, 1)
    # gen 2nd number
    b = random.randrange(1, 9, 1)
    return f"{a}x{b}"


if __name__ == "__main__":
    main()
