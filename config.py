import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002@localhost/blogs'


    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Kolems Blog!'
    SENDER_EMAIL = 'edwinkolem5@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002@localhost/blogs_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://edu:kmox002@localhost/blogs'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
