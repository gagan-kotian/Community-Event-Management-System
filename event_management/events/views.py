
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .forms import UserRegistrationForm,EventForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .models import Event


def home(request):
    return render(request, 'events/home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'events/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page after login
        else:
            return render(request, 'events/login.html', {'error': 'Invalid credentials'})
    return render(request, 'events/login.html')


from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Set the event organizer as the logged-in user
            event.save()
            return redirect('home')  # Redirect to the home page or an event list page
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch the event by ID
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)  # Bind the form to the event instance
        if form.is_valid():
            form.save()  # Save the updated event
            return redirect('event_list')  # Redirect to the event list after editing
    else:
        form = EventForm(instance=event)  # Pre-fill the form with event data
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch the event by ID
    if request.method == 'POST':
        event.delete()  # Delete the event
        return redirect('event_list')  # Redirect to the event list after deletion
    return render(request, 'events/delete_event.html', {'event': event})
