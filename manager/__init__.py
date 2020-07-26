from flask import Flask, request
from flask_login import current_user, login_required
from itsdangerous import URLSafeTimedSerializer
from manager.ext import csrf, db, login_manager,dbt
from manager.models import *
from manager.apps import *


def create_app():

    app = Flask(__name__, instance_relative_config=False)
    
    app.config.from_object('config.DevConfig')

    with app.app_context():
        register_apps(app)        
        extensions(app)
        authentication(app, Users)    

        
    return app


def extensions(app):    
    csrf.init_app(app)
    db.init_app(app)
    dbt.init_app(app)
    login_manager.init_app(app)    

    return None

def register_apps(app):    
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(sales)
    app.register_blueprint(customers)
    app.register_blueprint(inventory)
    app.register_blueprint(suppliers)

    return None


def authentication(app, user_model):
    login_manager.login_view = 'users.login'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)

    # @login_manager.token_loader
    # def load_token(token):
    #     duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
    #     serializer = URLSafeTimedSerializer(app.secret_key)

    #     data = serializer.loads(token, max_age=duration)
    #     user_uid = data[0]

    #     return user_model.query.get(user_uid)
