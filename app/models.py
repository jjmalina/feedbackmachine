from django.db import models


class Event(models.Model):
    """Model for a DemoDays event
    """
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    url = models.URLField(help_text='The Meetup URL')
    current_demo = models.ForeignKey('Demo', related_name='presenting_events', null=True)


class Demo(models.Model):
    event = models.ForeignKey('Event', related_name='demos')
    presenter = models.CharField(max_length=40, help_text='The presenter\'s name')
    email = models.EmailField()
    twitter = models.CharField(max_length=15, blank=True)
    url = models.URLField(blank=True)


class Comment(models.Model):
    demo = models.ForeignKey('Demo', related_name='comments')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
