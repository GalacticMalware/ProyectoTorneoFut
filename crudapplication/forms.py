from django import forms
from crudapplication.models import Fut, Partido
from crudapplication.models import Fut2



class FutForm(forms.ModelForm):
	class Meta:
		model = Fut
		fields = "__all__"



class FutForm2(forms.ModelForm):
	class Meta:
		model = Fut2
		fields = "__all__"




class PartidoForm(forms.ModelForm):
	class Meta:
		model = Partido
		fields = "__all__"

