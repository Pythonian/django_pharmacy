from django.contrib import admin

from .models import (Company, Medicine, EmployeeSalary,
                     BillDetails, CustomerRequest, CompanyAccount,
                     CompanyBank, Bill, Customer, Employee)

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
