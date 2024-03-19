from django.shortcuts import render
from .models import Todo


def home(request):
    all = Todo.objects.all()
    return render(request,'home.html',context = {'todos':all})

def sayhello(request):
    person = {
        "name" : 'amirhamzh',
    }
    return render(request,'hello.html',context = person)

