# coding: utf-8
from .default import Config


class DevelopmentConfig(Config):
    # App config
    DEBUG = True

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/dianchang-admin"
    SQLALCHEMY_BINDS = {'dc': "mysql+pymysql://root:@localhost/dianchang"},
    ROOT_TOPIC_ID = 1,
    PRODUCT_TOPIC_ID = 2,
    ORGANIZATION_TOPIC_ID = 3,
    POSITION_TOPIC_ID = 4,
    SKILL_TOPIC_ID = 5,
    PEOPLE_TOPIC_ID = 6,
    OTHER_TOPIC_ID = 7,
    NC_TOPIC_ID = 8,
    CDN_HOST = "http://xxx.qiniudn.com",
    DC_DOMAIN = "http://localhost:5000"
