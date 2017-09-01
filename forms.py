from django import forms
from .models import *


class hrmsForm(forms.ModelForm):
	class Meta:
		model = hrms
		fields = '__all__'

class educationForm(forms.ModelForm):
	class Meta:
		model = education
		fields = ('Education', 'Date', 'Grade', 'Remark', 'School')