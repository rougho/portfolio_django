from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form}) 