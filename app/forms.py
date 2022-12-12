from django import forms
from app.models import *


class POST_VIEWS_FORM(forms.ModelForm):
    class Meta:
        model=job_post
        fields = '__all__'
        widgets = {
            'job_profile':forms.TextInput(attrs={'class':'form-control'}),
            'company_name':forms.TextInput(attrs={'class':'form-control'}),
            'job_location':forms.TextInput(attrs={'class':'form-control'}),
            'min_salary':forms.NumberInput(attrs={'class':'form-control'}),
            'max_salary':forms.NumberInput(attrs={'class':'form-control'}),
            'package':forms.TextInput(attrs={'class':'form-control'}),
            'Vacancy':forms.NumberInput(attrs={'class':'form-control'}),
            'job_description':forms.Textarea(attrs={'class':'form-control'}),
            # 'job_skill':forms.Textarea(attrs={'class':'form-control'}),
            # 'job_experience':forms.Textarea(attrs={'class':'form-control'}),
        }
