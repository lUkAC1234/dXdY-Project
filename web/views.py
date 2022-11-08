import kwargs as kwargs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import requests
from .forms import RegistrationForm, LoginForm, UserModel, AccountForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from .forms import BlogModelForm
from web.models import BlogModel
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound


def smth(request):
    template_name = 'main/index.html'
    return render(request, template_name, context={
        
    })


def smth2(request):
    template_name = 'main/other_pages/index2.html'
    return render(request, template_name, context={

    })

def smth3(request):
    if request.user.is_authenticated:
        return redirect('error')
    else:
        form = LoginForm()

        template_name = 'main/other_pages/index3.html'
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = authenticate(
                    username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password']
                )
                if user is not None:
                    login(request, user)
                    return redirect('main')
                form.add_error('username', 'Username or password is incorrect')
        return render(request, template_name, context={
            'login_form': form,
        })

@login_required()
def logout_view(request):
    logout(request)
    return redirect('main')

def smth4(request):
    template_name = 'main/other_pages/index4.html'
    return render(request, template_name, context={

    })

def smth5(request):
    if request.user.is_authenticated:
        return redirect('error')
    else:
        form = RegistrationForm()
        template_name = 'main/other_pages/index5.html'
        if request.method == 'POST':
            form = RegistrationForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                del form.cleaned_data['confirm_password']
                user = UserModel(
                    username=form.cleaned_data['username'],
                    password = make_password(form.cleaned_data['password'])
                )
                user.save()
                return redirect('login')
            raise ValidationError(form.errors)

        return render(request, template_name, context={

    })


@login_required()
def smth6(request):
    form1 = AccountForm(instance=request.user)
    if request.method == 'POST':
        form1 = AccountForm(data=request.POST, files=request.FILES, instance=request.user)
        if form1.is_valid():
            user = get_object_or_404(UserModel, id=request.user.id)
            user.save()
            form1.save()
            request.user.user_image = form1
            return redirect('main')
    template_name = 'main/other_pages/index6.html'
    return render(request, template_name, context={
        'account_form': form1,
    })

@login_required()
def smth7(request):

    blogs = BlogModel.objects.all()

    template_name = 'main/other_pages/index7.html'
    return render(request, template_name, context={
        'blogs': blogs
    })

@login_required()
def form(request):

    form = BlogModelForm()
    if request.method == 'POST':
        form = BlogModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('myblogs')

    template_name = 'main/other_pages/index8.html'
    return render(request, template_name, context={
        'create_form': form,
    })



@login_required()
def blog_detail(request, id):
    template_name = 'main/other_pages/index9.html'
    blog = BlogModel.objects.get(id=id)
    blog.view_click += 1
    blog.save()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = blog
            data.save()
            return redirect('myblogs')
    return render(request, template_name, context={
        'blog': blog,
        'comment_form': form,
    })

def error_view(request, *args, **kwargs):
    text = render_to_string('main/other_pages/404.html')
    return HttpResponseNotFound(text)