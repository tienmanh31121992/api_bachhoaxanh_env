import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khoa-bi-mat-cua-toi'


class DevelopmentConfig(Config):
    """
    Cấu hình môi trường development
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Cấu hình môi trường production
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
