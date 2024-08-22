from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from .models import Booking, Room

# Booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'data'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('room'),
                Field('usage'),
                Div(
                    Field('start_time'),
                    css_class='control is-expanded'
                ),
                Div(
                    Field('end_time'),
                    css_class='control is-expanded'
                ),
                css_class='field is-grouped'
            ),
            Field('request')
        )


# Room
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'data'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('status'),
            Div(
                Div(
                    Field('name'),
                    css_class='control is-expanded'
                ),
                Field('floor'),
                Div(
                    Field('capacity'),
                ),
                css_class='field is-grouped'
            ),
            Field('facility')
        )