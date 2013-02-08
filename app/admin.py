from django.contrib import admin
from app.models import Event, Demo, Comment

class EventAdmin(admin.ModelAdmin):
    pass

class DemoAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Demo, DemoAdmin)
admin.site.register(Comment, CommentAdmin)