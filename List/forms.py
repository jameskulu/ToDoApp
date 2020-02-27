from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control border rounded-pill text-light',
            'placeholder':'Add Tasks',
            'autocomplete':'off',
            'style':'background-color:rgba(0,0,0,0) !important;'
    }
    ))
    
    class Meta:
        model = Task
        fields = '__all__'