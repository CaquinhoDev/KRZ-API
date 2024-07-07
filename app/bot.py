from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import os
from spacy.cli import download


# Database URI
DATABASE_URI = "sqlite:////data/krzbot.sqlite3"

# Training file path
TRAINER_FILEPATH = "./app/trainer.json"

# First run file
FIRST_RUN_FILEPATH = '/data/firstRun.krz'

# Is this the first run?
FIRST_RUN = not os.path.isfile(FIRST_RUN_FILEPATH)


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


def __setup():
    if not os.path.isdir('/data'):
        os.mkdir('/data')


if FIRST_RUN:
    __setup()
    with open(FIRST_RUN_FILEPATH, "w") as f:
        f.write("Krz")


download("en_core_web_sm")

chatbot = ChatBot("KrzBot", tagger_language=ENGSM, database_uri=DATABASE_URI)


if FIRST_RUN:
    # Load conversation list from training file
    with open(TRAINER_FILEPATH, 'r', encoding='utf-8') as trainer_file:
        conversations = json.load(trainer_file)

    trainer = ListTrainer(chatbot)
    trainer.train(conversations)