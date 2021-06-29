from celery import shared_task
from .models import Announcement, User
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from MMORPG_ANNOUNCEMENTS.settings import DEFAULT_FROM_EMAIL


@shared_task
def action():
    new_anns = Announcement.objects.filter(article_time_in__gt=datetime.now() - timedelta(days=7))
    list_of_emails = []
    for user in User.objects.all():
        list_of_emails.append(user.email)
    html_context = {'new_anns': new_anns}
    html_content = render_to_string('mail_week_notification.html', html_context)
    msg = EmailMultiAlternatives(
        subject='Новые объявления на MMORPG-announcements',
        from_email=DEFAULT_FROM_EMAIL,
        to=list_of_emails
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
