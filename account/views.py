from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import loginForm, signForm
from django.contrib.auth import login, authenticate, logout
from .models import User

def logOut(req):
    try:
        logout(req)
        return redirect('/')
    except:
        return HttpResponse("Error")

def loginFr(req):
    if req.method == 'POST':
        form = loginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(req, username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    print(req)
                    login(req, user)
                    return redirect('/')
                else:
                    return HttpResponse('disable')
            else:
                return HttpResponse('not found invalid')

    else:
        form = loginForm()
    return render(req, "account/login.html", {'form': form})

def signFr(req):
    if req.method == 'POST':
        form = signForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd["username"]
            password = cd["password"]
            email = cd["email"]
            user = User.objects.create_user(username, email, password)
            if user is not None:
                return redirect("/account/login")
    else:
        form = signForm()

    return render(req, "account/signup.html", {'form': form})
