from django.urls import path, include
from django.conf.urls import url
from . import views

#Django admin header customiztaion

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.login, name="login"),
]