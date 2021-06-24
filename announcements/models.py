from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(models.Model):
    cat_name = models.CharField(max_length=255, verbose_name='Category name')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Announcement(models.Model):
    ann_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author of announcement')
    ann_title = models.CharField(max_length=255, verbose_name='Announcement title')
    ann_body = RichTextField(blank=True, null=True, verbose_name='Announcement')
    ann_time_in = models.DateTimeField(auto_now_add=True, verbose_name='Time of announcement creation')
    ann_category = models.ManyToManyField(Category, verbose_name='Category of announcement')

    def __str__(self):
        return self.ann_title

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'


class Comment(models.Model):
    com_ann = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name='Commented announcement')
    com_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author of comment')
    com_body = models.TextField(verbose_name='Comment')
    com_time_in = models.DateTimeField(auto_now_add=True, verbose_name='Time of comment creation')
    com_confirmed = models.BooleanField(default=False, verbose_name='Comment confirmed by announcement author')

    def __str__(self):
        return f'{self.com_author}: "{self.com_body}"'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
