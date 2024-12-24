from django.forms import ModelForm
from .models import MailModel


class MailForm(ModelForm):
    class Meta:
        model = MailModel
        fields = ['to', 'subject', 'message']