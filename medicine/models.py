from django.db import models

from account.models import Employee, User


class Company(models.Model):
    name = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Companies'

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
    bank_account_no = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
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
    cost_price = models.CharField(max_length=255)
    sale_price = models.CharField(max_length=255)
    shelf_no = models.CharField(max_length=255)
    expiry_date = models.DateField()
    manufacturing_date = models.DateField()
    manufacturer = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    in_stock_total = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomerRequest(models.Model):
    PENDING = 'P'
    DONE = 'D'
    STATUS_CHOICE = (
        (PENDING, 'Pending'),
        (DONE, 'Done'),)
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    medicine_details = models.CharField(max_length=255)
    status = models.CharField(
        'Request status', max_length=1, choices=STATUS_CHOICE, default=PENDING)
    added_on = models.DateTimeField('Requested on', auto_now_add=True)
    prescription = models.FileField(blank=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.customer_name


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(
        max_digits=15, decimal_places=2,
        blank=True, null=True)
    sold_by = models.ForeignKey(User, related_name='sold_medicines', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bill: {self.customer}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    # get_total_cost.allowed_tags = True

    def save(self, *args, **kwargs):
        # self.unit_price = self.medicine.sell_price
        # self.total_amount = self.quantity * self.unit_price
        self.total_amount = self.get_total_cost()
        super().save(*args, **kwargs)


class BillDetails(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # sold_by = models.ForeignKey(Employee, related_name='sold_medicines')
    added_on = models.DateTimeField(auto_now_add=True)

    @property
    def get_cost(self):
        return self.medicine.sale_price

    @property
    def get_total_cost(self):
        return self.get_cost * self.quantity
