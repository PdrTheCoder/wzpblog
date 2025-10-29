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

    # load system env & load config
    flask_env = os.environ.get('FLASK_ENV', 'development')
    if flask_env == 'development' :
        cfg = import_string('blog_api.config.DevelopmentConfig')()
    elif flask_env == 'testing':
        # TODO
        cfg = import_string('blog_api.config.TestingConfig')()
    elif flask_env == 'production':
        # TODO
        cfg = import_string('blog_api.config.ProductionConfig')()
    else:
        exit(1)
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
