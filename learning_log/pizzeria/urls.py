# define pizzeria url pattern

from django.conf.urls import url

from . import views

app_name = 'pizzeria'
urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),

    # pizzas
    url(r'^/pizzas/$', views.pizzas, name='pizzas'),

    # pizza
    url(r'^/pizzas/(?P<pizza_id>d+)$', views.pizza, name='pizza'),
]