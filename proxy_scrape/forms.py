from django import forms
from .models import ScrapeJob

class ScrapeJobForm(forms.ModelForm):
    class Meta:
        model = ScrapeJob
        fields = "__all__"