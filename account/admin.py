from django.contrib import admin

from .models import User, Administrator, Employee, EmployeeSalary


class EmployeeSalaryInline(admin.TabularInline):
    model = EmployeeSalary
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'joined_date', 'phone', 'address', 'bank_name', 'bank_account_no']
    list_filter = ['joined_date']
    search_fields = ['name', 'joined_date', 'bank_name']
    inlines = [EmployeeSalaryInline]

admin.site.register([User, Administrator])
