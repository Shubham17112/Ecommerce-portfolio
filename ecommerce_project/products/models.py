from django.db import models
from tinymce.models import HTMLField  # Use TinyMCE for the text editor
from django.views.generic import ListView, DetailView
from django.db.models import Q

# models.py
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    
    location = models.CharField(max_length=200,null=True, blank=True)
    date = models.CharField(max_length=200,null=True, blank=True)
    detail_date = models.CharField(max_length=200,null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="events")
    image = models.ImageField(upload_to="events/", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])


class EventDetail(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='detail')
    image1 = models.ImageField(upload_to="event_details/", null=True, blank=True)
    image2 = models.ImageField(upload_to="event_details/", null=True, blank=True)
    image3 = models.ImageField(upload_to="event_details/", null=True, blank=True)
    description = HTMLField()

    def __str__(self):
        return f"Details for {self.event.title}"

    
# Booking Model
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    additional_info = HTMLField(blank=True, null=True)  # Optional description
    image_1 = models.ImageField(upload_to="bookings/", blank=True, null=True)
    image_2 = models.ImageField(upload_to="bookings/", blank=True, null=True)
    image_3 = models.ImageField(upload_to="bookings/", blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.event.title} by {self.name}"
    
    
    
    
    
class PopularEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    month = models.CharField(max_length=20)  # Alternatively, calculate from `date`
    place = models.CharField(max_length=255)
    detail_date = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.name



from django.db import models

class EmailSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
