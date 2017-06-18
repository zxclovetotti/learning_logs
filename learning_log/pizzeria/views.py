from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Pizza

def index(request):
    # homepage of pizzeria
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    # show all menu
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/pizzas.html', context)

def pizza(request, pizza_id):
    # show all details
    pizza = Pizza.object.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria/pizza.html', context)