from django import forms
from ..models import Team

class AthleteForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = '__all__'
