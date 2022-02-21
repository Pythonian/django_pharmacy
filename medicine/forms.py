from django import forms

from .models import (
    Company, CompanyBank, Medicine, MedicalDetails, CompanyAccount, Customer,
    Employee, EmployeeBank, EmployeeSalary, CustomerRequest, Bill, BillDetails)


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
    class Meta:
        model = CompanyAccount
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeBankForm(forms.ModelForm):
    class Meta:
        model = EmployeeBank
        fields = "__all__"


class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = "__all__"


class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = "__all__"


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
