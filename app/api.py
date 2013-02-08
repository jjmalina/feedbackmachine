from tastypie.resources import ModelResource
from app.models import Event, Demo, Comment


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'


class DemoResource(ModelResource):
    class Meta:
        queryset = Demo.objects.all()
        resource_name = 'demo'


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
