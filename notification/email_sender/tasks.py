import smtplib
from email.mime.text import MIMEText

from django.conf import settings
from notification.celery import celery_app


@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 2, 'countdown': 2},
)
def send_registartion_email(
        self, receiver_email, confirm_url, sender_email, sender_password,
):
    if settings.DEBUG:
        return confirm_url

    msg = MIMEText(
        'Для подтверждения аккаунта перейдите по ссылке %s.' % confirm_url,
    )
    msg['Subject'] = 'Подтверждение аккаунта'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, [receiver_email], msg.as_string())
    server.quit()
    return confirm_url
