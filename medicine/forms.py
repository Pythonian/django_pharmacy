from django import forms

from .models import (
    Company, CompanyBank, Medicine, MedicalDetails, CompanyAccount, Customer,
    Employee, EmployeeSalary, CustomerRequest, Bill, BillDetails)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['added_on']


class CompanyBankForm(forms.ModelForm):
    class Meta:
        model = CompanyBank
        fields = ['bank_account_no', 'ifsc_no']


class MedicineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medical_type'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Medicine
        exclude = ['added_on']


class MedicalDetailsForm(forms.ModelForm):
    class Meta:
        model = MedicalDetails
        fields = "__all__"


class CompanyAccountForm(forms.ModelForm):
    transaction_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['transaction_type'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['transaction_amt'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['payment_mode'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = CompanyAccount
        exclude = ['added_on']


class EmployeeForm(forms.ModelForm):
    joined_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['bank_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['bank_account_no'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = Employee
        exclude = ['added_on']


class EmployeeSalaryForm(forms.ModelForm):
    salary_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salary_amount'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = EmployeeSalary
        exclude = ['employee', 'added_on']


class CustomerRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['medicine_details'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['prescription'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = CustomerRequest
        fields = ['customer_name', 'phone',
                  'medicine_details', 'prescription']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"


class BillDetailsForm(forms.ModelForm):
    class Meta:
        model = BillDetails
        fields = "__all__"
