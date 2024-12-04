from django.contrib import admin
from .models import Category, Event, PopularEvent, EmailSubscription,EventDetail

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display these fields in the admin list view
    search_fields = ('name',)  # Add a search bar for the 'name' field

# Event Admin

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'date', 'detail_date')  # Customize the list view
    list_filter = ('categories', 'location', 'date')  # Add filters for these fields
    search_fields = ('title', 'location')  # Add a search bar for 'title' and 'location'
    filter_horizontal = ('categories',)  # Make ManyToManyField manageable in admin

# PopularEvent Admin
@admin.register(PopularEvent)
class PopularEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'month', 'place', 'detail_date')
    search_fields = ('name', 'place', 'detail_date')

# EmailSubscription Admin
admin.site.register(EmailSubscription)
@admin.register(EventDetail)
class EventDetailAdmin(admin.ModelAdmin):
    list_display = ('event', 'get_event_title', 'get_event_date')
    search_fields = ('event__title',)

    def get_event_title(self, obj):
        return obj.event.title
    get_event_title.short_description = 'Event Title'

    def get_event_date(self, obj):
        return obj.event.date
    get_event_date.short_description = 'Event Date'
