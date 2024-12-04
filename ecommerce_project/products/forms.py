from django import forms
from .models import EmailSubscription

class EmailSubscriptionForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'flex-grow px-4 py-2 rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Enter email address',
        'aria-label': 'Email for newsletter'
    }))
    class Meta:
        model = EmailSubscription
        fields = ['email']
