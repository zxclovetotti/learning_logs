from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
    # homepage of leanring logs
    return render(request, 'learning_logs/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def topics(request):
    # show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    # display detail info of specific topic
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    # add new topic
    if request.method != 'POST':
        # create a new form if no submit received
        form = TopicForm()
    else:
        # process submitted data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)