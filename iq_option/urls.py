from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('iqlogin', views.iq_option_login),
    path('login', views.login)
]
