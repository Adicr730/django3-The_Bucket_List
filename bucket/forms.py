from django.forms import ModelForm
from .models import Bucket

class BucketForm(ModelForm):
	class Meta:
		model = Bucket
		fields = ['title', 'details', 'datetocomplete', 'priority'] 
