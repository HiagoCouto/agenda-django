from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_event', 'created_at')
    list_filter = ('title', 'date_event',)

admin.site.register(Event, EventAdmin)
