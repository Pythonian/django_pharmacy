from django.contrib import admin

from .models import (Company, Medicine, BillDetails, CustomerRequest, CompanyAccount,
                     CompanyBank, Bill, Customer)


class BillDetailInline(admin.StackedInline):
    model = BillDetails
    extra = 1


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['customer', 'added_on']
    inlines = [BillDetailInline]


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'medical_type', 'cost_price', 'sale_price', 'expiry_date', 'in_stock_total']
    list_filter = ['medical_type', 'manufacturer', 'expiry_date']
    search_fields = ['name', 'medical_type', 'description']
    date_hierarchy = 'added_on'


class CompanyBankInline(admin.StackedInline):
    model = CompanyBank
    extra = 1


class CompanyAccountInline(admin.StackedInline):
    model = CompanyAccount
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'license_no', 'address', 'contact_no', 'email']
    search_fields = ['name', 'email']
    inlines = [CompanyBankInline, CompanyAccountInline]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'address', 'added_on']
    search_fields = ['name', 'contact']
    date_hierarchy = 'added_on'


@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone', 'medicine_details', 'status', 'added_on']
    list_filter = ['status']
    search_fields = ['medicine_details', 'customer_name']
    date_hierarchy = 'added_on'
