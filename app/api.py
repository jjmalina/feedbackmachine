from tastypie.resources import ModelResource
from app.models import Event, Demo, Comment


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'


class DemoResource(ModelResource):
    class Meta:
        queryset = Demo.objects.all()
        resource_name = 'demos'


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comments'
