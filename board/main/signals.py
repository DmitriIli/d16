from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import Reply
from .tasks import send_mail_new_reply


@receiver(post_save, sender=Reply)
def create_reply(sender, instance, created, **kwargs):

    if created:
        email_list = []
        reply_author = Reply.objects.filter(pk=instance.id).select_related(
            'author').select_related('user').values('text', 'author__username', 'author__email')
        ads = Reply.objects.filter(pk=instance.id).select_related(
            'ads').select_related('author').select_related('user').values('ads__author__username', 'ads__title')
        ads_author_name = ads.first().get('ads__author__username')
        ads_title = ads.first().get('ads__title')
        reply_author = reply_author.first().get('author__username')

        send_mail_new_reply.delay(
            email_list=email_list, recipient=ads_author_name, reply_author=reply_author, title=ads_title)

        # email_list.append(reply_author.first().get('author__email'))
        # ads_author_name = ads.first().get('ads__author__username')
        # ads_title = ads.first().get('ads__title')
        # reply_author = reply_author.first().get('author__username')
        # send_mail(
        #     f'Приветсвую тебя {ads_author_name}',
        #     f'На твоё объявление {ads_title} ответил пользователь {reply_author}',
        #     'softb0x@yandex.ru',
        #     email_list,
        #     fail_silently=False,
        # )

    return redirect('/')
