# Import flask and template operators
import sys
from flask import Flask
import logging

# Define the WSGI application object
bot_app = Flask(__name__)

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


from app.chatbot.api.views import bot_app as bot_api_module
from app.chatbot.webui.views import bot_ui as bot_ui_module

# Register blueprint(s)
bot_app.register_blueprint(bot_api_module)
bot_app.register_blueprint(bot_ui_module)
