import urllib
import hashlib

from django.db import models


class EventManager(models.Manager):
    """docstring for EventManager"""
    def current(self):
        current_events = Event.objects.filter(
            is_current=True).order_by('-datetime')
        if current_events:
            return current_events[0]
        return None


class Event(models.Model):
    """Model for a DemoDays event
    """
    objects = EventManager()
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    url = models.URLField(help_text='The Meetup URL')
    current_demo = models.ForeignKey(
        'Demo', related_name='presenting_events', null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Demo(models.Model):
    event = models.ForeignKey('Event', related_name='demos')
    presenter = models.CharField(max_length=40, help_text='The presenter\'s name')
    email = models.EmailField()
    twitter = models.CharField(max_length=15, blank=True)
    title = models.CharField(max_length=15, blank=True)
    description = models.CharField(max_length=144, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.presenter

    @models.permalink
    def get_absolute_url(self):
        return ('app.views.demo', [self.id])

    def _get_gravatar_url(self, size):
        default = 'http://placehold.it/64x64'
        url = 'http://www.gravatar.com/avatar/%s?%s' % (
            hashlib.md5(self.email.lower()).hexdigest(),
            urllib.urlencode({'d':default, 's':str(size)}))
        return url

    avatar = property(lambda self: self._get_gravatar_url(64))


class Comment(models.Model):
    demo = models.ForeignKey('Demo', related_name='comments')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
