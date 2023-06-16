
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse


from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Login'}


@login_required(login_url='login')
def profile(request):
    users = Main.objects.all()

    context = {
        'users': users,
        'title': 'User Manager Dashboard'
    }

    return render(request, 'user/profile.html', context)


@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddUserForm()
    context = {
        'form': form,
        'title': 'Add New User'
    }
    return render(request, 'user/add_user.html', context)


@login_required(login_url='login')
def edit(request, pk):
    user = Main.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=user)
    context = {
        'title': 'Update User',
        'form': form
    }
    return render(request, 'user/edit_profile.html', context)


@login_required(login_url='login')
@csrf_exempt
def delete(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        Main.objects.get(id=user_id).delete()
        return JsonResponse({'bool': True})
