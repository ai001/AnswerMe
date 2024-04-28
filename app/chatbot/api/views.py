# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, url_for
import logging
from app.chatbot.chatter.bot import bot, default_answer
from app.chatbot.config.qanda import QnA

from app import bot_app

bot_app = Blueprint('bot_app', __name__, url_prefix='/backend/chatbot/api/v1')

bot_api = Api(bot_app)

parser = reqparse.RequestParser()
parser.add_argument('question', type=str, required=True, help='Please ask something!')

for (q, a) in QnA:
    bot.train([q, a])

class getResponse_api(Resource):
    def get(self):
        args = parser.parse_args()
        question = args['question']
        answer = bot.get_response(question)
        status = { 'success': True, 'result_length': len(str(answer))}
        response = {'data': { 'question': question, 'response': str(answer) }, 'status': status}

        # loggin bit
        if (str(answer) == default_answer):
            logging.warn("WARN - MISS - " + question + ": " + str(answer))
            #print (str(datetime.now()) + ',' + 'MISS' + ',' + question)
        else:
            #print (str(datetime.now()) + ',' + 'HIT' + ',' + question)
            logging.info("INFO - HIT - " + question + ": " + str(answer))
        
        return response

bot_api.add_resource(getResponse_api, '/getResponse')
