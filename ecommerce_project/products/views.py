from django.shortcuts import render, get_object_or_404
from .models import Category, Event, Booking
from django.shortcuts import render, redirect
from .forms import EmailSubscriptionForm

from .models import PopularEvent


def index(request):
    events = PopularEvent.objects.all()
    
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a "Thank You" page after subscription
    else:
        form = EmailSubscriptionForm()
    
    context = {
        'events': events,
        'form': form,
    }
    
    return render(request, 'products/hero/index.html', context)

def thank_you(request):
    return render(request, 'products/hero/thank_you.html')



# views.py
from django.shortcuts import render, get_object_or_404
from .models import Event, Category

def event_list(request):
    categories = Category.objects.all()
    events = Event.objects.all()

    selected_categories = request.GET.getlist("categories")
    if selected_categories:
        events = events.filter(categories__id__in=selected_categories).distinct()

    return render(request, "products/event_list.html", {
        "categories": categories,
        "events": events,
        "selected_categories": list(map(int, selected_categories)),
    })


# View for handling bookings
def booking_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        additional_info = request.POST.get("additional_info")
        image_1 = request.FILES.get("image_1")
        image_2 = request.FILES.get("image_2")
        image_3 = request.FILES.get("image_3")

        # Create the booking
        booking = Booking.objects.create(
            event=event,
            name=name,
            email=email,
            phone_number=phone_number,
            additional_info=additional_info,
            image_1=image_1,
            image_2=image_2,
            image_3=image_3,
        )
        return render(request, 'products/booking_success.html', {'booking': booking})
    return render(request, 'products/booking_form.html', {'event': event})





################
from django.shortcuts import render
from django.views.generic import ListView
from .models import Event, Category

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'  # Your template for the event list
    context_object_name = 'events'
    
    def get_queryset(self):
        queryset = Event.objects.all()  # Start with all events

        # Get selected category IDs from request GET parameters
        selected_category_ids = self.request.GET.getlist('category')

        if selected_category_ids:
            # Filter events by selected category IDs
            queryset = queryset.filter(categories__id__in=selected_category_ids).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Provide all categories to the template
        context['categories'] = Category.objects.all()
        # Pass selected category IDs to the template
        context['selected_categories'] = [int(id) for id in self.request.GET.getlist('category')]
        return context


from django.views.generic import DetailView
from .models import Event, EventDetail

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_detail'] = EventDetail.objects.get(event=self.object)
        return context

