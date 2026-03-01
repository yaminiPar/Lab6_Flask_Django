from django.shortcuts import render
from .models import Message

# homepage
def home(request):
    return render(request, 'home.html')

# greeting page
def greet(request, name):
    return render(request, 'greet.html', {'name': name})

# message list page
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'messages.html', {'messages': messages})