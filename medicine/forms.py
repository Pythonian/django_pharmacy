from django import forms
from django.forms import formset_factory, BaseModelFormSet, ModelChoiceField

from account.models import EmployeeSalary, Employee

from .models import (
    Company, CompanyBank, Medicine, CompanyAccount, Customer,
    CustomerRequest, Bill, BillDetails)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['added_on']


class CompanyBankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bank_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['bank_account_no'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = CompanyBank
        fields = ['bank_account_no', 'bank_name']


class MedicineForm(forms.ModelForm):
    expiry_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control'}))
    manufacturing_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['manufacturer'].widget.attrs.update({'class': 'form-control'})
        self.fields['medical_type'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['cost_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['sale_price'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['expiry_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['manufacturing_date'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['shelf_no'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['in_stock_total'].widget.attrs.update(
            {'class': 'form-control'})
        
    class Meta:
        model = Medicine
        exclude = ['added_on']


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
        self.fields['status'].widget.attrs.update(
            {'class': 'form-select form-control'})

    class Meta:
        model = CustomerRequest
        fields = ['customer_name', 'phone',
                  'medicine_details', 'prescription', 'status']


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Customer
        fields = "__all__"


class BillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Bill
        fields = "__all__"
        # fields = ['customer', 'total_amount']

class CustomerBillForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    
    customer = ModelChoiceField(queryset=Customer.objects.all())


class BillDetailsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    medicine = ModelChoiceField(queryset=Medicine.objects.all(),)
    quantity = forms.IntegerField(max_value=100, min_value=1)

BillDetailsFormset = formset_factory(BillDetailsForm, extra=1)

