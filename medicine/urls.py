from django.urls import path
from . import views


urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('company/create/', views.company_create, name='company_create'),
    path('company/<int:id>/', views.company_detail, name='company_detail'),
    path('company/<int:id>/bank/create/',
         views.company_bank_create, name='company_bank_create'),
    path('company/<int:company_id>/bank/<int:bank_id>/update/',
         views.company_bank_update, name='company_bank_update'),

    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicine/create/', views.medicine_create, name='medicine_create'),
    path('medicine/<int:id>/', views.medicine_update, name='medicine_update'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_create, name='customer_create'),

    path('company/accounts/',
         views.company_account_list, name='company_account_list'),
    path('company/account-create/',
         views.company_account_create, name='company_account_create'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/<int:id>/update/',
         views.employee_update, name='employee_update'),
    path('employee/<int:id>/salary-create/',
         views.employee_salary_create, name='employee_salary_create'),

    path('generate-bill/', views.generate_customer_bill, name='create_bill'),
    path('submit-bill/', views.submit_customer_bill, name='submit_bill'),

    path('customer-requests/',
         views.customer_requests, name='customer_requests'),
    path('customer-requests/create/',
         views.create_customer_requests, name='create_customer_requests'),
     path('customer-request/<int:id>/', views.customer_request, name='customer_request'),
]
