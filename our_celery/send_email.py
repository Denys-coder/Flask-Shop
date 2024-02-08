import yagmail
from celery import Celery
from properties.mail import *

app = Celery('send_email', broker='pyamqp://guest@localhost//')


@app.task
def send_successful_order_email(item_dicts):
    body = "Your ordered:"
    for e in item_dicts:
        body += "item name: " + e["name"]
        body += "item description: " + e["description"]
        body += "item price: " + e["price"]
        body += "item category: " + e["category"]
        body += "quantity: " + e["quantity"]
        body += "<hr>"
    subject = "Your order"
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(to=receiver_email, subject=subject, contents=body)
