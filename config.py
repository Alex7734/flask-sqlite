from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

    from modules.users.routes import users
    from modules.problems.routes import problems
    from util.modal_clear_routes import modal_clear

    app.register_blueprint(users)
    app.register_blueprint(modal_clear)
    app.register_blueprint(problems)

    from util.database import init_db
    init_db()

    return app
