from multiprocessing import context
from pyexpat import model
from attr import fields
from django.shortcuts import redirect, render
from . models import Work
from . import forms
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
    work_list=Work.objects.all()
    return render(request,'testapp/home.html',{'work_list':work_list})

def signup_view(request):
    form=forms.SignUpform()
    if request.method=='POST':
        form=forms.SignUpform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form}) 

def logout_view(request):
    return render(request,'testapp/logout.html')   

'''    

def delete_view(request,id):
    work_list=Work.objects.get(id=id)
    work_list.delete()
    return redirect('/home')

def Update_view(request,id):
    work_list=Work.objects.get(id=id)
    print(request.method)
    if request.method=="POST":
        form=forms.Update_form(request.POST,instance=work_list)
        print('balu')
        if form.is_valid():
            form.save()
        print('##################')
        print('#####################')    
        print(form.errors)    
        return HttpResponseRedirect('/home')
    return render(request,'testapp/update.html',{'work_list':work_list})  '''

class WorkCreate_view(CreateView):
    model=Work
    fields=['place','Name','about_work','choose','amount','status']

class WorkUpdate_view(UpdateView):
    model=Work
    fields=['place','Name','about_work','choose','amount']  

class WorkDelete_view(DeleteView):
    model=Work  
    success_url=reverse_lazy('home')    




















    