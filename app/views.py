from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from app.models import Event, Demo, Comment

import json


def current_demo(request, event_id):
    event = Event.objects.get(id=event_id)
    current_demo_json = json.dumps({
        'demo_id': event.current_demo.id
    })
    return HttpResponse(current_demo_json)


@csrf_exempt
@require_POST
def create_comment(request, demo_id):
    comment = Comment.objects.create(
        demo_id=demo_id, content=request.POST.get('content'))
    comment_json = json.dumps({
        'demo_id': comment.demo_id,
        'created_at': str(comment.created_at),
        'content': comment.content
    })
    return HttpResponse(comment_json)


def index(request):
    event = Event.objects.current()
    return render(request, 'index.html', {
        'event': event,
        'current_demo': event.current_demo,
        'demos': event.demos.all()
    })


def demo(request, demo_id):
    demo = Demo.objects.get(id=demo_id)
    event = Event.objects.get(id=demo.event.id)
    current_demo = event.current_demo
    return render(request, 'demo.html', {
        'event': event,
        'demo': demo,
        'current_demo': current_demo
    })
