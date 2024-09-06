from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Add a new task',
            'class': 'form-control'
        })
    )
    add_notes = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Add notes',
            'class': 'form-control',
            'rows': 5  # Adjust height as needed
        }),
        required=False  # Make this field optional if desired
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Task
        fields = "__all__"