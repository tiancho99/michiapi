import os
import json

with open(os.path.abspath(f"{os.environ.get('MICHIAPI_CONFIG')}")) as config_file:
    conf = json.load(config_file)

class Config:
    DEBUG = conf.get('DEBUG')
    SECRET_KEY = conf.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = conf["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_ECHO = conf.get("SQLALCHEMY_ECHO")
    WTF_CSRF_SECRET_KEY = conf.get("WTF_CSRF_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data', 'michis.db')
    UPLOAD_FOLDER = "static/images/"
    
