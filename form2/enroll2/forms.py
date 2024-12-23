from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    first_name=forms.CharField()

class field(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

class field2(forms.Form):
    name=forms.CharField(error_messages={'required':"enter the name"})
    roll=forms.IntegerField(min_value=4,max_value=10)
    price=forms.DecimalField(min_value=5,max_value=40,max_digits=4,decimal_places=1)
    rate=forms.FloatField(min_value=5,max_value=40)
    comment=forms.SlugField(max_length=200)
    email=forms.EmailField(min_length=5,max_length=50)
    website=forms.URLField(min_length=5,max_length=50)
    password=forms.CharField(min_length=5,max_length=50,widget=forms.PasswordInput)
    description=forms.CharField(widget=forms.Textarea)
    feedback=forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={"class":"somecss1 somecss2","id":"uniqueid"}))
    notes=forms.CharField(widget=forms.Textarea(attrs={"rows":3,"cols":4}))
    agree=forms.BooleanField(label="i agree")