from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name = 'signup'),
    url(r'^login/', auth_views.login, {'template_name': 'accounts/login.html'}, name = 'login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name = 'logout'),
]
