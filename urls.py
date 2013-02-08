from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from app.api import EventResource, DemoResource, CommentResource


v1_api = Api(api_name='v1')
v1_api.register(EventResource())
v1_api.register(DemoResource())
v1_api.register(CommentResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='index'),
    url(r'^home$', 'app.views.index', name='index'),
    url(r'^demo/(\d+)/$', 'app.views.demo', name='demo'),

    url(r'^json/events/(\d+)/current_demo/$', 'app.views.current_demo', name='current_demo'),
    url(r'^json/demos/(\d+)/comments/$', 'app.views.create_comment', name='create_comment'),

    # url(r'^feedbackmachine/', include('feedbackmachine.foo.urls')),

    (r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
