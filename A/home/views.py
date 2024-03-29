from django.shortcuts import redirect , render
from .models import Todo
from django.contrib import messages
from .forms import TOdoCreateForm,TOdoUpdateForm


def home(request):
    all = Todo.objects.all()
    return render(request,'home.html',context = {'todos':all})


def detail(request,todo_id):
        todo = Todo.objects.get(id = todo_id)
        return render(request,'detail.html',context={'todo':todo}) 

def delete(request,todo_id):
    Todo.objects.get(id =todo_id).delete()
    messages.success(request,"todo deleted successfully",'success')
    return  redirect('home')

def create(request):
    if request.method == 'POST':
        form = TOdoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title = cd['title'],body = cd['body'],created = cd['created'])
            messages.success(request,'todo created successfuly','success')
            return redirect('home')
    else:
        form = TOdoCreateForm()
    return render(request,'create.html',{'form':form})


def update (request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = TOdoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,"todo updated successfully",'success')
            return redirect('details',todo_id)
    else:
        form = TOdoUpdateForm(instance = todo)
    return render(request,'update.html',{'form':form})

