from django.shortcuts import render
from enroll2.forms import StudentRegistration,field,field2
# Create your views here.

def showformdata(request):
    form=StudentRegistration(auto_id=True,label_suffix="-",initial={"name":"Binod"})
    form.order_fields(field_order=['first_name','email','name'])
    return render(request,'enroll2/userregistration.html',{"form1":form})

def fieldshow(request):
    if request.method=="POST":
        fm=field(request.POST)
        print(fm)
    else:
        fm=field()
        print('get request form')
    return render(request,'enroll2/field.html',{"form2":fm})



def fieldshow2(request):
    if request.method=="POST":
        fm2=field2(request.POST)
        if fm2.is_valid():
             print("form validated")
             print("Name",fm2.cleaned_data['name'])
             print("roll",fm2.cleaned_data['roll'])
             print("price",fm2.cleaned_data['price'])
             print("rate",fm2.cleaned_data['rate'])
             print("rate",fm2.cleaned_data['rate'])
             print("comment",fm2.cleaned_data['comment'])
             print("email",fm2.cleaned_data['email'])
             print("website",fm2.cleaned_data['website'])
             print("password",fm2.cleaned_data['password'])
             print("description",fm2.cleaned_data['description'])
             print("feedback",fm2.cleaned_data['feedback'])
             print("Agree",fm2.cleaned_data['agree'])      
    else:
        fm2=field2()
        print("hello")
    return render(request,'enroll2/field2.html',{"form3":fm2})