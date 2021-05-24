from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signupview(request):
    template_name = 'englishapp/list.html'
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request, 'user/signup.html',{'error':'このユーザーは既に登録されています'})
    else:
        return render(request, 'user/signup.html',{})
    return render(request, template_name,{})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data,password=password_data)
        if user is not None:
            login(request, user)
            return redirect('englishapp:index')
        else:
            return redirect('user:login')
    return render(request, 'user/login.html',{})

def logoutview(request):
    logout(request)
    return redirect('user:login')