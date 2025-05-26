from django import forms
from .models import DailyEntry

class DailyEntryForm(forms.ModelForm):
    class Meta:
        model = DailyEntry
        fields = ['mood']
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
        }
