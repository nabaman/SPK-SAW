from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect


def loginView(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            redirect('login')

    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')