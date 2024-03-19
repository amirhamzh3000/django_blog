from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def sayhello(request):
    person = {
        "name" : 'amirhamzh',
    }
    return render(request,'hello.html',context = person)

