from django import forms

from .models import (
    Company, CompanyBank, Medicine, CompanyAccount, Customer,
    Employee, EmployeeSalary, CustomerRequest, Bill, BillDetails)


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
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['medical_type'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['buy_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['sell_price'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['c_gst'].widget.attrs.update({'class': 'form-control'})
        self.fields['s_gst'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['batch_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['shelf_no'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['salt_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['salt_quantity'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['in_stock_total'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['quantity_in_strip'].widget.attrs.update(
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
        fields = ['customer_name', 'customer_address', 'customer_phonenumber']


class BillDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = BillDetails
        fields = ['medicine', 'quantity']
