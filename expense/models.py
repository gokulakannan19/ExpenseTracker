from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birth_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username


class Expense(models.Model):

    CATEGORY_HOUSEHOLD = "H"
    CATEGORY_ENTERTAINMENT = "E"
    CATEGORY_BILL = "B"
    CATEGORY_MEDICINE = "M"
    CATEGORY_TRAVEL = "T"

    CATEGORY_CHOICES = [
        (CATEGORY_ENTERTAINMENT, "Entertainment"),
        (CATEGORY_HOUSEHOLD, "Household"),
        (CATEGORY_BILL, "Bill"),
        (CATEGORY_MEDICINE, "Medicine"),
        (CATEGORY_TRAVEL, "Travel"),
    ]

    PAYMENT_TYPE_CREDIT_CARD = "CC"
    PAYMENT_TYPE_DEBIT_CARD = "DC"
    PAYMENT_TYPE_UPI = "UPI"
    PAYMENT_TYPE_NETBANKING = "NB"
    PAYMENT_TYPE_OFFLINE = "OFF"

    PAYMENT_TYPE_CHOICES = [
        (PAYMENT_TYPE_CREDIT_CARD, "Credit Card"),
        (PAYMENT_TYPE_DEBIT_CARD, "DEBIT Card"),
        (PAYMENT_TYPE_UPI, "UPI"),
        (PAYMENT_TYPE_NETBANKING, "Net Banking"),
        (PAYMENT_TYPE_OFFLINE, "Offline"),
    ]

    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPE_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
