import os
from os import urandom

class config:
    random_hex=urandom(16).hex()
    SECRET_KEY=random_hex
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =25
    MAIL_USE_TLS=False
    MAIL_USE_SSL=False
    
