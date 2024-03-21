from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home),
    path('hello/',views.sayhello),
    path('detail/<int:todo_id>',views.detail),

]