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

# class field3(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput)

#     def clean_name(self):
#         valname=self.cleaned_data['name']
#         if len(valname)<4:
#             raise forms.ValidationError("enter more than or equal 4 character")
#         return valname

class field3(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data['name']
        valemail=self.cleaned_data['email']
        if len(valname)<4:
            raise forms.ValidationError("name shold be more than or equal 4")
        
        if len(valemail)<10:
            raise forms.ValidationError("email should be more than or equal 10")
        
class field4(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    Rpassword=forms.CharField(widget=forms.PasswordInput,label="password(again)")
    def clean(self):
        cleaned_data=super().clean()
        valpw=self.cleaned_data['password']
        valrpw=self.cleaned_data['Rpassword']
        if valpw!=valrpw:
            raise forms.ValidationError("Password does not match")