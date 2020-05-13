import os
from os import urandom
from PIL import Image
from flask_mail import Message
from flask import url_for,current_app

def save_picture(form_picture):
    random_hex=urandom(8).hex()
    _,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(current_app.root_path, 'static/profile', picture_fn)
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token =user.get_reset_token()
    msg=Message('Password Reset Request',sender='ngupta7_be17@thapar.edu', recipients=[user.email])
    msg.body=f'''To reset your password,vist this link:-
{url_for('users.reset_token',token=token,_external=True)}

If you did not make this request simply ignore this.
'''
    mail.send(msg)
