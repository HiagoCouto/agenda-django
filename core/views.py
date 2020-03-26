from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha errados")

    return redirect('/')

@login_required(login_url='/login/')
def index(request):
    user = request.user
    events = Event.objects.filter(user=user)
    data = {
            'events': events,
            'user': user,
            }
    return render(request, 'schedule.html', data)

@login_required(login_url='/login/')
def store(request):
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        date_event = request.POST.get('date_event')
        hour_event = request.POST.get('hour_event')
        user = request.user

        datetime_event = date_event + ' ' + hour_event

        Event.objects.create(title=title,
                description=description,
                date_event=datetime_event,
                user=user)
    return redirect('/')

