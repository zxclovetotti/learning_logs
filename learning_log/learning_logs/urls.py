# define learning_logs url pattern

from django.conf.urls import url

from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),
]