from django.urls import path
from enroll2 import views
urlpatterns = [
    path('registration/',views.showformdata),
    path('',views.fieldshow),
    path('field2',views.fieldshow2),
    path('field3',views.fieldshow3),
    path('field4',views.fieldshow4),


]
