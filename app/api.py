from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from app.models import Event, Demo, Comment


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        authorization = Authorization()
        resource_name = 'events'
        allowed_methods = ['get']

class DemoResource(ModelResource):
    class Meta:
        queryset = Demo.objects.all()
        authorization = Authorization()
        resource_name = 'demos'
        allowed_methods = ['get']


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        authorization = Authorization()
        resource_name = 'comments'
