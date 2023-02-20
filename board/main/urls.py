from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mainview, name='main'),
    path('create/', editads, name='create'),
    path('<int:pk>', DetailAds.as_view(), name='detail'),
    path('<int:pk>/edit', UpdateAds.as_view(), name='edit'),
    path('<int:pk>/reply', ReplyOnAds.as_view(), name='reply'),
]