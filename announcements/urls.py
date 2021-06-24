from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('ann/<int:pk>', PersonalAccount.as_view(), name='ann_detail'),
    path('logout/', logout, name='logout'),
]
