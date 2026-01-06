from django.forms import ModelForm
from .models import LogIn


class LogInForm(ModelForm):
    class Meta:
        model = LogIn
        fields = [__all__]