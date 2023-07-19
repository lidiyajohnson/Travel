from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo')
    # path('sub/',views.subtraction,name='subtraction'),
    # path('add/',views.addition,name='addition')
]
