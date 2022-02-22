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

    path('company/accounts/',
         views.company_account_list, name='company_account_list'),
    path('company/account-create/',
         views.company_account_create, name='company_account_create'),
]
