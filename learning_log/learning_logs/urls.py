# define learning_logs url pattern

from django.conf.urls import url

from . import views

# template can not be used if app_name missing
app_name = 'learning_logs'
urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),

    # display topics
    url(r'^topics/$', views.topics, name='topics'),
    
    # display topic detail
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # display topics
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]