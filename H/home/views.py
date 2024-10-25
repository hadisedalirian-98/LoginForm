from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm,TodoUpdateForm

# Create your views here.

def home(request):
    all =Todo.objects.all()
    return render(request, 'home.html',{'todos':all})





def detail(request, todo_id):
    todo =Todo.objects.get(id=todo_id)
    return render(request, 'detail.html',{'todo':todo})



def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'you delete your post succeessfully','success')
    return redirect('home')

 

def create(request):  
    form = TodoCreateForm()  
    if request.method == 'POST':  
        form = TodoCreateForm(request.POST)  
        if form.is_valid():  
            cd = form.cleaned_data  
            Todo.objects.create(  
                title=cd['title'],  
                body=cd['body'],  
                created=cd['created']  
            )  
            messages.success(request, 'You created your post successfully.', 'success')  
            return redirect('home')  
    
 
    return render(request, 'create.html', {'form': form})

def update(request, todo_id):  
    todo =Todo.objects.get(id=todo_id)
    form = TodoUpdateForm(request.POST, instance=todo)  
    if request.method == 'POST':   
        if form.is_valid():   
            form.save()  
            messages.success(request, 'You updated your post successfully.', 'success')  
            return redirect('details', todo_id)  
    else:
        return render(request, 'update.html', {'form': form})           

    