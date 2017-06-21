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

    # add new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing a new entry.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]