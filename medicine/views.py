from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import (BillDetailsForm, BillForm, CompanyAccountForm,
                    CompanyBankForm, CompanyForm, CustomerForm,
                    CustomerRequestForm, EmployeeBankForm, EmployeeForm,
                    EmployeeSalaryForm, MedicalDetailsForm, MedicineForm)
from .models import (Bill, BillDetails, Company, CompanyAccount, CompanyBank,
                     Customer, CustomerRequest, Employee, EmployeeBank,
                     EmployeeSalary, MedicalDetails, Medicine)


#### COMPANY VIEWS ####

@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(
        request, 'company/list.html', {'companies': companies})


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company details successfully created.')
            return redirect('company_list')
    else:
        form = CompanyForm()

    return render(request, 'company/form.html', {'form': form, 'create': True})


@login_required
def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company details successfully updated.')
            return redirect('company_detail', company.id)
        else:
            messages.warning(request, 'An error occured. Check below.')
    else:
        form = CompanyForm(instance=company)
    return render(
        request, 'company/detail.html',
        {'company': company, 'form': form})


@login_required
def company_bank_create(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyBankForm(request.POST)
        if form.is_valid():
            company_bank = form.save(commit=False)
            company_bank.company = company
            company_bank.save()
            messages.success(
                request, 'Company Bank details successfully created.')
            return redirect('company_detail', company.id)
        else:
            messages.warning(
                request, 'There was a problem saving this data.')
    else:
        form = CompanyBankForm()

    return render(request, 'company/bank_form.html',
                  {'form': form, 'create': True, 'company': company})


@login_required
def company_bank_update(request, company_id, bank_id):
    company = get_object_or_404(Company, id=company_id)
    company_bank = get_object_or_404(
        CompanyBank, id=bank_id, company=company)
    if request.method == 'POST':
        form = CompanyBankForm(request.POST, instance=company_bank)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Company Bank details successfully updated.')
            return redirect('company_detail', company.id)
        else:
            messages.warning(request, 'An error occured. Check below.')
    else:
        form = CompanyBankForm(instance=company_bank)

    return render(request, 'company/bank_form.html',
                  {'form': form, 'company': company,
                   'company_bank': company_bank})


@login_required
def company_account_list(request):
    company_accounts = CompanyAccount.objects.all()
    return render(request, 'company/account_list.html',
                  {'company_accounts': company_accounts})


@login_required
def company_account_create(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyAccountForm(request.POST)
        if form.is_valid():
            company_account = form.save(commit=False)
            company_account.company = company
            company_account.save()
            messages.success(
                request, 'Company Account data successfully created.')
            return redirect('company_detail', company.id)
        else:
            messages.warning(
                request, 'Error occured during saving of this data.')
    else:
        form = CompanyBankForm()

    return render(request, 'company/account_form.html',
                  {'form': form, 'create': True, 'company': company})


#### MEDICINE VIEWS ####

@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(
        request, 'medicine/list.html', {'medicines': medicines})


@login_required
def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine data successfully created.')
            return redirect('medicine_list')
        else:
            messages.warning(request, 'There was an issue identified below')
    else:
        form = MedicineForm()
    return render(request, 'medicine/form.html',
                  {'form': form, 'create': True})


@login_required
def medicine_update(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine data successfully updated.')
            return redirect('medicine_list')
        else:
            messages.warning(request, 'An error occured. Check below.')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'medicine/form.html',
                  {'form': form, 'medicine': medicine})
