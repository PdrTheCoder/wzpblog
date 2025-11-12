import os

from flask import Flask
from flask_cors import CORS
from werkzeug.utils import import_string
from flask_jwt_extended import JWTManager

from blog_api.models import db
from blog_api.blogs_bp import bp as blog_blueprint
from blog_api.auth import bp as auth_blueprint
from blog_api.error_handler import register_err_handler


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False

    # load cfg variables from env
    app.config['SECRET_KEY'] = os.environ.get(
        'SECRET_KEY',
        'bro_forgot_set_secret_key_dammmmn'
    )

    app.config['JWT_SECRET_KEY'] = os.environ.get(
        'JWT_SECRET_KEY',
        'bro_forgot_set_jwt_secret_key_dammmmn'
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        exit(1)


    # load from object
    cfg = import_string('blog_api.config.Config')()
    app.config.from_object(cfg)

    # jwt part
    jwt = JWTManager(app)

    # db part
    db.init_app(app)

    # register blueprints
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(auth_blueprint)

    # register error handler
    register_err_handler(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)
    
    return app
