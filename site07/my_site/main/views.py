from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page.html")

def page1(request):
    return render(request, "main/page1.html")

def page2(request):
    return render(request, "main/page2.html")

def page3(request):
    return render(request, "main/page3.html")

def page4(request):
    return render(request, "main/page4.html")

def page5(request):
    return render(request, "main/page5.html")

def page6(request):
    return render(request, "main/page6.html")

def page7(request):
    return render(request, "main/page7.html")

def page8(request):
    return render(request, "main/page8.html")

def test(request):
    return render(request, "main/test.html")

def profile(request):
    return render(request, "main/profile.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
