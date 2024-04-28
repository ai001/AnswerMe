# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from datetime import datetime
from app.chatbot.config.qanda import QnA

default_answer = 'I am sorry, I do not understand.'

bot = ChatBot(
    'Terminator',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database="database.db",
    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        # # {
        # #      'import_path': 'chatterbot.logic.MathematicalEvaluation',
        # # },
        # {
        #      'import_path': 'chatterbot.logic.TimeLogicAdapter',
        # },
        {
             'import_path': 'chatterbot.logic.LowConfidenceAdapter',
             'threshold': 0.65,
             'default_response': default_answer
         }
    ],
    #filters=["chatterbot.filters.RepetitiveResponseFilter"],
    trainer='chatterbot.trainers.ListTrainer'
)
