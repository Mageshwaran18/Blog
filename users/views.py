from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account successfully created for {username}log in now!!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})
@login_required
def profile(request):
    return render(request, 'users/profile.html')


def custom_logout(request):
    logout(request)
    return redirect('logoutt')

def logout_form(request):
    return render(request, 'users/logoutt.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST,instance = request.user)
        p_form = ProfileUpdate(request.POST,request.FILES,instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your Profile was Updated!!!")
            return redirect('profile')
    else:
        u_form = UserUpdate(instance = request.user)
        p_form = ProfileUpdate(instance = request.user.profile)
    context = {"u_form":u_form,
            "p_form":p_form}
    return render(request, 'users/profile_update.html',context)