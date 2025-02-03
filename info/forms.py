from django import forms
from . models import members_model,accesories_model,Trainers_model,transactions_model
from django.core.validators import RegexValidator
class members_form(forms.ModelForm):
        name = forms.CharField(
        max_length=100,  # You can adjust the max length as per your requirement
        required=False,
        validators=[RegexValidator(r'^[A-Za-z ]+$', 'Only letters and spaces are allowed in name.')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'})
    )
        class Meta:
            model = members_model
            fields = '__all__'
            widgets = {
                'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name',}),
                'phone_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'phone_no'}),
                'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
                'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'duration'}),
                'trainer':forms.TextInput(attrs={'class':'form-control','placeholder': 'Bob,huma,smith.....'}),
            }

class accesories_form(forms.ModelForm):
    class Meta:
        model = accesories_model
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'qauntity':forms.NumberInput(attrs={'class':'form-control','placeholder':'name'}),
            'maintenance':forms.DateInput(attrs={'class':'form-control','placeholder':'name'}),
        }

class Trainers_form(forms.ModelForm):
    class Meta:
        model = Trainers_model
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'phone_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'name'}),
            'payscale':forms.NumberInput(attrs={'class':'form-control','placeholder':'name'}),

            'join_date':forms.TextInput(attrs={'class':'form-control','placeholder':'name'})

        }

class transactions_form(forms.ModelForm):
    class Meta:
        model = transactions_model
        fields = '__all__'
        widgets = {
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'date':forms.TextInput(attrs={'class':'form-control','placeholder':'date'})

        }
