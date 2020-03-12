from flask_mail import Message
from app import app,mail
from threading import Thread


def send_async_mail(msg,app):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body,html_body):
    msg=Message(subject,sender=sender,recipients=[recipients])
    msg.body = text_body
    msg.html = html_body
    t1 = Thread(target=send_async_mail,args=(msg,app)).start()


