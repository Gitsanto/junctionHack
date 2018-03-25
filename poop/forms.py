from django import forms

from poop.models import dataset

class upload_dataset(forms.ModelForm):
    class Meta:
        model = dataset
        fields = ['dataset_image',]
