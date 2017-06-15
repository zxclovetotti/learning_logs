# define learning_logs url pattern

from django.conf.urls import url

from . import views

# template can not be used if app_name missing
app_name = 'learning_logs'
urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),
]