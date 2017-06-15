from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Topic

def index(request):
    # homepage of leanring logs
    return render(request, 'learning_logs/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def topics(request):
    # show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)