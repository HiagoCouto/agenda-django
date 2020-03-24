from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):
    user = request.user
    events = Event.objects.filter(user=user)
    data = {
            'events': events,
            'user': user,
            }
    return render(request, 'schedule.html', data)
