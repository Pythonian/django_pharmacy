import datetime
from datetime import timedelta
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from medicine.models import (
    CustomerRequest, Bill, Medicine, Company, Employee, BillDetails)

from .models import User
from .forms import (
    AdministratorSignUpForm, PharmacistSignUpForm)


@login_required
def home(request):
    if request.user.is_administrator:
        return redirect('administrator_dashboard')
    else:
        return redirect('pharmacist_dashboard')


class AdministratorSignUpView(CreateView):
    model = User
    form_class = AdministratorSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'an administrator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('administrator_dashboard')


class PharmacistSignUpView(CreateView):
    model = User
    form_class = PharmacistSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'a pharmacist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pharmacist_dashboard')


@login_required
def administrator_dashboard(request):
    customer_request = CustomerRequest.objects.all().count()
    bill_count = Bill.objects.all().count()
    medicine_count = Medicine.objects.all().count()
    company_count = Company.objects.all().count()
    employee_count = Employee.objects.all().count()

    bill_details = BillDetails.objects.all()
    profit_amt = 0
    sell_amt = 0
    buy_amt = 0
    for bill in bill_details:
        buy_amt = float(
            buy_amt + float(bill.medicine.buy_price)) * int(bill.qty)
        sell_amt = float(
            sell_amt + float(bill.medicine.sell_price)) * int(bill.qty)
    profit_amt = sell_amt - buy_amt

    customer_request_pending = CustomerRequest.objects.filter(
        status=False).count()

    customer_request_completed = CustomerRequest.objects.filter(
        status=True).count()

    current_date = datetime.date.today().strftime("%Y-%m-%d")
    current_date1 = datetime.date.today()
    current_date_7days = current_date1 + timedelta(days=7)
    current_date_7days = current_date_7days.strftime("%Y-%m-%d")
    bill_details_today = BillDetails.objects.filter(
        added_on__date=current_date)
    profit_amt_today = 0
    sell_amt_today = 0
    buy_amt_today = 0
    for bill in bill_details_today:
        buy_amt_today = float(
            buy_amt_today + float(bill.medicine.buy_price)) * int(bill.qty)
        sell_amt_today = float(
            sell_amt_today + float(
                bill.medicine.sell_price)) * int(bill.qty)
    profit_amt_today = sell_amt_today - buy_amt_today

    medicine_expire = Medicine.objects.filter(
        expiry_date__range=[current_date, current_date_7days]).count()

    bill_dates = BillDetails.objects.order_by().values(
        'added_on__date').distinct()
    profit_chart_list = []
    sell_chart_list = []
    buy_chart_list = []
    for billdate in bill_dates:
        access_date = billdate['added_on__date']
        bill_data = BillDetails.objects.filter(added_on__date=access_date)
        profit_amt_inner = 0
        sell_amt_inner = 0
        buy_amt_inner = 0
        for billsingle in bill_data:
            buy_amt_inner = float(
                buy_amt_inner + float(
                    billsingle.medicine.buy_price)) * int(billsingle.qty)
            sell_amt_inner = float(
                sell_amt_inner + float(
                    billsingle.medicine.sell_price)) * int(billsingle.qty)
        profit_amt_inner = sell_amt_inner - buy_amt_inner

        profit_chart_list.append(
            {"date": access_date, "amt": profit_amt_inner})
        sell_chart_list.append(
            {"date": access_date, "amt": sell_amt_inner})
        buy_chart_list.append({"date": access_date, "amt": buy_amt_inner})

    return render(
        request, 'administrator_index.html',
        {'customer_request': customer_request,
         'bill_count': bill_count,
         'medicine_count': medicine_count,
         'company_count': company_count,
         'employee_count': employee_count,
         'profit_amt': profit_amt,
         'customer_request_pending': customer_request_pending,
         'customer_request_completed': customer_request_completed,
         'profit_amt_today': profit_amt_today,
         'medicine_expire': medicine_expire,
         'sell_amt': sell_amt})


@login_required
def pharmacist_dashboard(request):

    return render(
        request, 'pharmacist_index.html',
        {})
