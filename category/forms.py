from django import forms

from .models import Animal, Description

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['text']
        labels = {'text': ''}
        
        
class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['text']
        labels = {'text': 'Description:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}