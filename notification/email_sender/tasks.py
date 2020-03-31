from notification.celery import celery_app


@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 5, 'countdown': 2},
)
def send_registartion_email(self, email, confirm_url):
    return confirm_url
