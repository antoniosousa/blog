from django import forms

from publication.models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['pub_title', 'pub_text', 'pub_image']
        widgets = {
            'pub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication title'}),
            'pub_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter publication text', 'rows': 4}),
            'pub_image': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
        }