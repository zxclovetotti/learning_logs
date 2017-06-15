from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # homepage of pizzeria
    return render(request, 'pizzeria/index.html')
