from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def registrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario-login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/registrar.html', context)
