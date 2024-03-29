from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reporte.models import Reporte
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET","POST"])  # Sensitive
def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})


@require_http_methods(["GET","POST"])  # Sensitive
@login_required
def profile(request):

    

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'reportes': Reporte.objects.filter(autor=request.user.id)
    }

    return render(request, 'users/profile.html', context)
