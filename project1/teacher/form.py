from django import forms
from account.models import Mark,Student

class addmark_form(forms.ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'