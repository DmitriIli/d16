from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mainview, name='main'),
    path('create/', editads, name='create'),
    path('<int:pk>', DetailAds.as_view(), name='detail'),
    path('<int:pk>/edit', UpdateAds.as_view(), name='edit'),
    path('<int:pk>/reply', ReplyOnAds.as_view(), name='reply'),
    path('<str:name>', user_page, name='userpages'),
    path('<str:name>/<int:pk>/delete', ReplyDelete.as_view(), name='reply_delete'),
    path('<str:name>/<int:pk>/agry', reply_agry, name='reply_agry'),
]