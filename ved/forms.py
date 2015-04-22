from django.forms import ModelForm
from .models import Contact, HallBooking, PriestService
from django.forms import RadioSelect, BooleanField, TimeField, TextInput
from django.contrib.admin.widgets import AdminTimeWidget

class ContactForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets = { 
            'name': TextInput(attrs={'placeholder': 'Your Name'}), 
            'email': TextInput(attrs={'placeholder': 'myemail@email.com'}), 
            'subject': TextInput(attrs={'placeholder': 'Reason for contacting'}), 
            'booking_date': TextInput(attrs={'placeholder': '12/31/2015'}), 
        }

class HallForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = HallBooking
        fields = ['name','email','phone','booking_date','booking_time','priest_service_requested','comments']
        priest_service_requested = BooleanField(widget=RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))
        booking_time = TimeField(widget=AdminTimeWidget(format='%H:%M %p'))
        widgets = { 
            'name': TextInput(attrs={'placeholder': 'Your Name'}), 
            'email': TextInput(attrs={'placeholder': 'myemail@email.com'}), 
            'phone': TextInput(attrs={'placeholder': '(732) 555 1212'}), 
            'booking_date': TextInput(attrs={'placeholder': '12/31/2015'}), 
            'booking_time': TextInput(attrs={'placeholder': '11:00 AM'}), 
        }

class PriestServiceForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = PriestService
        fields = ['name','email','phone','pooja_date','pooja_time','pooja_type','pooja_location','comments']
        priest_service_requested = BooleanField(widget=RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))
        booking_time = TimeField(widget=AdminTimeWidget(format='%H:%M %p'))
        widgets = { 
            'name': TextInput(attrs={'placeholder': 'Your Name'}), 
            'email': TextInput(attrs={'placeholder': 'myemail@email.com'}), 
            'phone': TextInput(attrs={'placeholder': '(732) 555 1212'}), 
            'pooja_date': TextInput(attrs={'placeholder': '12/31/2015'}), 
            'pooja_time': TextInput(attrs={'placeholder': '11:00 AM'}), 
            'pooja_type': TextInput(attrs={'placeholder': 'Ex. Satyanarayan Pooja'}), 
            'pooja_location': TextInput(attrs={'placeholder': 'Ex. Home/Mandir'}), 
        }
