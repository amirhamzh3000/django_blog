from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def sayhello(request):
    return render(request,'hello.html')

