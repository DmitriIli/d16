from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.template.loader import render_to_string
from .models import Reply


@receiver(post_save, sender=Reply)
def create_reply(sender, instance, created, **kwargs):

    if created:
        email_list = []
        reply_author = Reply.objects.filter(pk=instance.id).select_related(
            'author').select_related('user').values('text', 'author__username', 'author__email')
        reply_ads_author = Reply.objects.filter(pk=instance.id).select_related(
            'ads').select_related('author').select_related('user').values('ads__author__username','ads__title')
        
        print(dict(reply_author))
        
        # email_list.append(str(instance.email))
        # html_content = render_to_string(
        #     'news/notify.html',
        #     {
        #         'instance': instance,
        #     }
        # )

        # msg = EmailMultiAlternatives(
        #     subject=f'Приветсвую тебя {instance.username}',
        #     body=f'Приветсвенное письмо для нового пользователя {instance.username}',
        #     from_email='softb0x@yandex.ru',
        #     to=email_list,
        # )
        # msg.attach_alternative(html_content, "text/html")  # добавляем html

        # msg.send()  # отсылаем

    return redirect('/')
