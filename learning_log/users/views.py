from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.

from django.contrib.auth import logout
def logout_view(request):
    # log out
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
