from django.contrib import admin

from .models import (Company, Medicine, EmployeeSalary,
                     BillDetails, CustomerRequest, CompanyAccount,
                     CompanyBank, Bill, Customer, Employee)


class BillDetailInline(admin.StackedInline):
    model = BillDetails


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    inlines = [BillDetailInline]

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(EmployeeSalary)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
