from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))