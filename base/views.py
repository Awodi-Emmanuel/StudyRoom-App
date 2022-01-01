from django.shortcuts import render
from django.http import HttpResponse

    # Create your views here.

#Dictionary
rooms = [
        {'id':1, 'name':'Lets learn python!'},
        {'id':2, 'name':'Design with me'},
        {'id':3, 'name':'frontend developer'},
    ]

def home(request): 
    context = {'rooms', rooms}
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')
