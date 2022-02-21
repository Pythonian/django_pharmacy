from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CompanyAccount(models.Model):
    DEBIT = 'D'
    CREDIT = 'C'
    TRANSACTION_TYPE_CHOICES = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        choices=TRANSACTION_TYPE_CHOICES,
        max_length=1)
    transaction_amt = models.CharField(max_length=255)
    transaction_date = models.DateField()
    payment_mode = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class CompanyBank(models.Model):
    # bank name
    bank_account_no = models.CharField(max_length=255)
    ifsc_no = models.CharField(max_length=255)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='banks')
    added_on = models.DateTimeField(auto_now_add=True)


class Medicine(models.Model):
    TABLET = 'T'
    SYRUP = 'S'
    MEDICAL_TYPE_CHOICES = (
        (TABLET, 'Tablet'),
        (SYRUP, 'Syrup'))

    name = models.CharField(max_length=255)
    medical_type = models.CharField(
        max_length=1, choices=MEDICAL_TYPE_CHOICES)
    buy_price = models.CharField(max_length=255)
    sell_price = models.CharField(max_length=255)
    c_gst = models.CharField(max_length=255)
    s_gst = models.CharField(max_length=255)
    batch_no = models.CharField(max_length=255)
    shelf_no = models.CharField(max_length=255)
    expiry_date = models.DateField()
    manufacturing_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    in_stock_total = models.IntegerField()
    quantity_in_strip = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MedicalDetails(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_quantity = models.CharField(max_length=255)
    salt_quantity_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    joined_date = models.DateField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class EmployeeBank(models.Model):
    bank_account_no = models.CharField(max_length=255)
    ifsc_no = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    medicine_details = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    prescription = models.FileField(default="")

    def __str__(self):
        return self.customer_name


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class BillDetails(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
