from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your Account has been created! You Can Now Login')
        return redirect ('login')
  else:
    form = UserRegisterForm()
  return render (request,'Users/Register.html', {'form': form})


#@login_requiredss
#def profile(request):
  #  return render(request, 'users/profile.html')
