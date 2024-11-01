from . models import Information
from django import forms

class infoform(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['task','date']
        error_messages = {
            'task':{'required':'name should be there'},
            'date':{'required':'Date is required'}
        }
        widgets ={
            'task':forms.Textarea(attrs={'rows':5,'cols':100}),
            'date':forms.Textarea(attrs={'rows':1})
            
        }
        labels = {
            'date':'Last Date'
        }


