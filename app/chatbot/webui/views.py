from flask import Blueprint, render_template

bot_ui = Blueprint('bot_ui', __name__, url_prefix='/bot_ui')


## Serve the home page
@bot_ui.route('/')
def index():
    return render_template('chatbot/chat_input.html')
