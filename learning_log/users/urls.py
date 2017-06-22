# define users url

from django.conf.urls import url
from django.contrib.auth.views import login

from .import views

app_name = 'users'
urlpatterns = [
    # login page
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
]