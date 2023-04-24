from django.core.mail import EmailMessage



def send_email(email_data):
    email = EmailMessage(
                    subject=email_data['email_subject'],
                    to=[email_data['email_to']],
                    body=email_data['email_body']
                )
    return email.send()

