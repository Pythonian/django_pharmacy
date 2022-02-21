from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import (
    AdministratorSignUpForm, PharmacistSignUpForm)


@login_required
def home(request):
    if request.user.is_administrator:
        return redirect('administrator_dashboard')
    else:
        return redirect('pharmacist_dashboard')


class AdministratorSignUpView(CreateView):
    model = User
    form_class = AdministratorSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'an administrator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('administrator_dashboard')


class PharmacistSignUpView(CreateView):
    model = User
    form_class = PharmacistSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'a pharmacist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pharmacist_dashboard')


@login_required
def administrator_dashboard(request):
    
    return render(
        request, 'administrator_index.html',
        {})


@login_required
def pharmacist_dashboard(request):
    
    return render(
        request, 'pharmacist_index.html',
        {})
