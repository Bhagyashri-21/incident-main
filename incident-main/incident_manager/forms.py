# forms.py

from django import forms
from .models import Company, Incident

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'contact_name', 'contact_mail', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class IncidentForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Incident
        fields = ['title', 'brief_description', 'severity', 'attack_type', 'attack_vector',
                  'description', 'action_to_patch', 'attachment', 'security_researcher', 'company']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'brief_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'severity': forms.Select(attrs={'class': 'form-control'}),
            'attack_type': forms.TextInput(attrs={'class': 'form-control'}),
            'attack_vector': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'action_to_patch': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'attachment': forms.FileInput(attrs={'class': 'form-control-file'}),
            'security_researcher': forms.TextInput(attrs={'class': 'form-control'}),
        }
