from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api

from app.api import EventResource, DemoResource, CommentResource


v1_api = Api(api_name='v1')
v1_api.register(EventResource())
v1_api.register(DemoResource())
v1_api.register(CommentResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
