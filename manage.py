import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from app import bot_app
manager = Manager(bot_app)

manager.add_command("runserver", Server(
    use_debugger=False,
    use_reloader=False,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)))
)

if __name__ == "__main__":
    manager.run()
    