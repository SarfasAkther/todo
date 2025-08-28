from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo


# Create your views here.
def home(request):
    
    if request.method=="POST":
        
        form=TodoForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("home")
    else:
        form=TodoForm()
    todo=Todo.objects.all()    
    kk={'form':form,
        'todos':todo}    
    return render(request,'index.html',kk)
def delete(request,id):
    if request.method=="POST":   
        deec=Todo.objects.get(id=id)
        deec.delete()
        return redirect("home")
    
def update(request,id):
    todo=Todo.objects.get(id=id)
    formss=TodoForm(instance=todo)
    context={
         'form':formss
    }
    if request.method=="POST":
        formss=TodoForm(request.POST,instance=todo)
        if formss.is_valid():
            formss.save()
            return redirect("home")
    return render(request,'update.html',context)
 