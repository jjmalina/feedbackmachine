from django.db import models


class Event(models.Model):
    """Model for a DemoDays event
    """
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    url = models.URLField(help_text='The Meetup URL')
    current_demo = models.ForeignKey('Demo', related_name='presenting_events', null=True)

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


class Comment(models.Model):
    demo = models.ForeignKey('Demo', related_name='comments')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
