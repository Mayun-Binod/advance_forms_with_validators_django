from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(label="first name",label_suffix="b",initial={"name":"binod"})
    email=forms.EmailField()