from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import BaseRegisterView, signup, activate

urlpatterns = [
     path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
     path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
     path('signup/', signup, name='signup'),
     path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 
     activate, name='activate'),
]