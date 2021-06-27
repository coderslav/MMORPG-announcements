from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('ann/<int:pk>', AnnDetails.as_view(), name='ann_details'),
    path('create/', AnnCreate.as_view(), name='create'),
    path('delete/<int:pk>', AnnDelete.as_view(), name='delete'),
    path('edit/<int:pk>', AnnEdit.as_view(), name='update'),
    path('comments/<int:pk>', CommentDetails.as_view(), name='comment_details'),
    path('comments/create/', CommentCreate.as_view(), name='comment_create'),
    path('comments/', CommentList.as_view(), name='comment_list'),
    path('comments/edit/<int:pk>', CommentEdit.as_view(), name='comment_edit'),
    path('comments/delete/<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('private/', PrivateAccount.as_view(), name='private_account'),
    path('private/delete/<int:pk>', CommentDeleteByAnnAuthor.as_view(), name='comment_delete_by_ann_author'),
]
