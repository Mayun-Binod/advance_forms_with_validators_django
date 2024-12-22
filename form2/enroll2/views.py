from django.shortcuts import render
from enroll2.forms import StudentRegistration
# Create your views here.

def showformdata(request):
    form=StudentRegistration(auto_id=True,label_suffix="-",initial={"name":"Binod"})
    form.order_fields(field_order=['first_name','email','name'])
    return render(request,'enroll2/userregistration.html',{"form1":form})
