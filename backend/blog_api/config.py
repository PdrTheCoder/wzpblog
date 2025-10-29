class Config(object):
    TESTING = False
    JWT_SECRET_KEY = 'iloveff14'

class Production(Config):
    DATABASE_URI = ''
    JWT_SECRET_KEY = 'ilovewow'


class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:wzpdev@localhost:5432/test'
    JWT_SECRET_KEY = 'ilovewow'


class TestingConfig(Config):
    DATABASE_URI = ''
    TESTING = True
    SECRET_KEY = 'testing'
    JWT_SECRET_KEY = 'ilovesword'
