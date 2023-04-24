from celery import shared_task
from utills.email import send_email


@shared_task
def task_send_email(email_data):
    send_email(email_data)
