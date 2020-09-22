import os

class Config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:Hellomoringa@localhost/pitch"
    UPLOAD_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'joeljuma08@gmail.com'
    MAIL_PORT = ''
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class testConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Hellomoringa@localhost/pitch'

class devConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Hellomoringa@localhost/pitch'
    DEBUG = True

config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
    # 'test':TestConfig
}