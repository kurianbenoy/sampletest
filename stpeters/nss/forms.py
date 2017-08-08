from django import forms
from .models import NssUpload

class NssUploadForm(forms.ModelForm):
	class Meta:
		model = NssUpload
		fields = ['title','description']