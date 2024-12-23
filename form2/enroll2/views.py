from django.shortcuts import render
from enroll2.forms import StudentRegistration,field,field2,field3,field4
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

def fieldshow3(request):
    if request.method=="POST":
        fm3=field3()
        if fm3.is_valid():
             print("form validated")
             print("Name",fm3.cleaned_data['name'])
             print("email",fm3.cleaned_data['email'])
             print("password",fm3.cleaned_data['password'])               
    else:
        fm3=field3()
    return render(request,'enroll2/field3.html',{"form4":fm3})

def fieldshow4(request):
    if request.method=="POST":
        fm4=field4()
        if fm4.is_valid():
             print("form validated")
             print("Name",fm4.cleaned_data['name'])
             print("email",fm4.cleaned_data['email'])
             print("password",fm4.cleaned_data['password'])  
             print("Rpassword",fm4.cleaned_data['Rpassword'])               
             
    else:
        fm4=field4()
    return render(request,'enroll2/field4.html',{"form5":fm4})