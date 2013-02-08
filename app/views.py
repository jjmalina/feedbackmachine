from django.shortcuts import render
from models import *


def index(request):
    event = Event.objects.get(id=1)
    return render(request, 'index.html', { 'demos': event.demos.all() })

def demo(request, id):
    demo = Demo.objects.get(id=id)
    return render(request, 'demo.html', { 'demo': demo })
