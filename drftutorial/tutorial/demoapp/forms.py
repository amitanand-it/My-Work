from django.forms import ModelForm
from demoapp.models import Demo

class DemoForm(ModelForm):
    class Meta:
        model=Demo
        fields='__all__'


