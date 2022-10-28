from django.shortcuts import render, redirect


from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate

def smth(request):
    
    template_name = 'main/index.html'
    return render(request, template_name, context={
        
    })

def smth2(request):
    
    template_name = 'main/other_pages/index2.html'
    return render(request, template_name, context={
        
    })

def smth3(request):
    form = LoginForm()

    template_name = 'main/other_pages/index3.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            form.add_error('password', 'Incorrect password')
    return render(request, template_name, context={
        'login_form' : form,
    })

def smth4(request):
    
    template_name = 'main/other_pages/index4.html'
    return render(request, template_name, context={
        
    })

def smth5(request):
    form = RegistrationForm()
    template_name = 'main/other_pages/index5.html'
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('/')

    return render(request, template_name, context={
        'form': form
    })

def weather(request):
    
    template_name = 'main/other_pages/index6.html'
    return render(request, template_name, context={
        
    })