from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def index(request):
    # homepage of meal_planner
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'meal_planner/index.html')
