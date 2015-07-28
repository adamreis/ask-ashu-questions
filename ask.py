#!usr/local/bin/python3

from slacker import Slacker
from random import shuffle
from time import sleep
import os

try:
    SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']
except KeyError:
    from secrets import SLACK_API_TOKEN

if __name__ == "__main__":
    slack = Slacker(SLACK_API_TOKEN)

    with open('questions.txt') as question_file:
        questions = question_file.readlines()
        while True:
            shuffle(questions)
            for question in questions:
                slack.chat.post_message('@ashu', question)
                sleep(600)
