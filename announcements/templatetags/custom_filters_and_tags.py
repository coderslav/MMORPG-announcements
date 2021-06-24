from django import template
from django.template.defaultfilters import stringfilter
from announcements.models import Comment

register = template.Library()


@register.filter(name='confirmed_comment_filter')
def confirmed_comment_filter(ann_object):
    return Comment.objects.filter(com_ann=ann_object, com_confirmed=True)


@register.filter(name='unconfirmed_comment_filter')
def unconfirmed_comment_filter(ann_object):
    return Comment.objects.filter(com_ann=ann_object, com_confirmed=False)


@register.filter(name='censor')
@stringfilter
def censor(value):
    forbidden_words = ["плохое слово 1", "плохое слово 2", "плохое слово 3"]
    f_words = [word for word in forbidden_words if word in value]
    if f_words:
        new_value = value
        for f_word in f_words:
            new_value = new_value.replace(f_word, f_word[0] + '*' * (len(f_word)-2) + f_word[-1])
        return new_value
    else:
        return value
