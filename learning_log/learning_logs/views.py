from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # homepage of leanring logs
    return render(request, 'learning_logs/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")