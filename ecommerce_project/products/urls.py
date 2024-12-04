from django.urls import path
from . import views
from products.views import index  # Import the index view
from .views import EventListView, EventDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("products/event_list/", views.event_list, name="event_list"),
    path('events/', EventListView.as_view(), name='event_list_view'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),

    path('', index, name='index'),  # Home page
    path('thank_you/', views.thank_you, name='thank_you'),  # Optional "Thank You" page
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
