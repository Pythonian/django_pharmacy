from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import (BillDetailsForm, BillForm, CompanyAccountForm,
                    CompanyBankForm, CompanyForm, CustomerForm,
                    CustomerRequestForm, EmployeeForm,
                    EmployeeSalaryForm, MedicineForm)
from .models import (Bill, BillDetails, Company, CompanyAccount, CompanyBank,
                     Customer, CustomerRequest, Employee,
                     EmployeeSalary, Medicine)


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


# COMPANY ACCOUNT

@login_required
def company_account_list(request):
    company_accounts = CompanyAccount.objects.all()
    return render(request, 'company/account_list.html',
                  {'company_accounts': company_accounts})


@login_required
def company_account_create(request):
    if request.method == 'POST':
        form = CompanyAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Company Account data successfully created.')
            return redirect('company_account_list')
        else:
            messages.warning(
                request, 'Error occured during saving of this data.')
    else:
        form = CompanyAccountForm()

    return render(request, 'company/account_form.html',
                  {'form': form, 'create': True})


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


#### EMPLOYEE ####

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(
        request, 'employee/list.html', {'employees': employees})


@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee data successfully created.')
            return redirect('employee_list')
        else:
            messages.warning(request, 'There was an issue identified below')
    else:
        form = EmployeeForm()
    return render(request, 'employee/form.html',
                  {'form': form, 'create': True})


@login_required
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Employee data successfully updated.')
            return redirect('employee_update', employee.id)
        else:
            messages.warning(request, 'There was an issue identified below')
    else:
        employee_form = EmployeeForm(instance=employee)
    return render(request, 'employee/form.html',
                  {'employee_form': employee_form, 'employee': employee})


@login_required
def employee_salary_create(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeSalaryForm(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            salary.employee = employee
            salary.save()
            messages.success(
                request, 'Employee salary data successfully created.')
            return redirect('employee_update', employee.id)
        else:
            messages.warning(request, 'There was an issue identified below')
    else:
        form = EmployeeSalaryForm()
    return render(request, 'employee/salary_form.html',
                  {'form': form, 'employee': employee})


#### GENERATE BILLS ####

def generate_customer_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bill successfully generated.')
            return redirect('/')
        else:
            messages.warning(request, 'There was an issue identified below')
    else:
        form = BillForm()
    return render(request, 'bill/form.html',
                  {'form': form})


#### CUSTOMER REQUESTS ####

@login_required
def customer_requests(request):
    requests = CustomerRequest.objects.all()
    return render(
        request, 'customer/requests.html', {'requests': requests})


@login_required
def create_customer_requests(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer request successfully created.')
            return redirect('customer_requests')
        else:
            messages.warning(request, 'An error occured. Check below.')
    else:
        form = CustomerRequestForm()

    return render(request, 'customer/request_form.html',
                  {'form': form, 'create': True})


@login_required
def customer_request(request, id):
    customer_request = get_object_or_404(CustomerRequest, id=id)
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST, instance=customer_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer request successfully updated.')
            return redirect('customer_request', customer_request.id)
        else:
            messages.warning(request, 'An error occured. Check below.')
    else:
        form = CustomerRequestForm(instance=customer_request)
    return render(
        request, 'customer/form.html',
        {'customer_request': customer_request, 'form': form})
