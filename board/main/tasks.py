from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_new_reply(email_list, recipient, reply_author, title):
    send_mail(
        f'Приветсвую тебя {recipient}',
        f'На твоё объявление {title} ответил пользователь {reply_author}',
        'softb0x@yandex.ru',
        email_list,
        fail_silently=False,
    )


@shared_task
def send_mail_reply_agry(email_list, recipient):
    send_mail(
        f'Приветсвую тебя {recipient}',
        f'На твой отзыв получен ответ',
        'softb0x@yandex.ru',
        email_list,
        fail_silently=False,
    )


