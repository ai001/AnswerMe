# Run a test server.
from app import bot_app
bot_app.run(host='0.0.0.0', port=8080, debug=False)
