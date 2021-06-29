from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from django.template.loader import render_to_string


@receiver(post_save, sender=Comment)
def new_comment(sender, instance, created, **kwargs):
    if created:
        print('Я тут!')
        html_context = {'new_comment': instance, 'ann': instance.com_ann, }
        html_content = render_to_string('mail_ann_author_notification.html', html_context)
        send_mail(
            subject='У вас новый отклик на сайте MMORPG-announcements',
            message=None,
            html_message=html_content,
            from_email=None,  # will use DEFAULT_FROM_EMAIL variable from settings.py
            recipient_list=[instance.com_ann.ann_author.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Comment)
def com_accepted(sender, instance, update_fields,  **kwargs):
    if update_fields and 'com_confirmed' in update_fields:
        html_context = {'comment': instance, 'ann': instance.com_ann, 'ann_id': instance.id}
        html_content = render_to_string('mail_com_author_notification.html', html_context)
        send_mail(
            subject='Ваш отклик на сайте MMORPG-announcements одобрен!',
            message=None,
            html_message=html_content,
            from_email=None,  # will use DEFAULT_FROM_EMAIL variable from settings.py
            recipient_list=[instance.com_ann.ann_author.email],
            fail_silently=False,
        )
