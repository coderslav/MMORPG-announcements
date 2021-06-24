from django.forms import ModelForm
from .models import Announcement, Comment


class AnnForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['ann_author', 'ann_title', 'ann_body', 'ann_category']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['com_author', 'com_ann', 'com_body']
