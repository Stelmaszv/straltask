from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

currency_choices =(
    ("EUR","EUR"),
    ("USD","USD"),
    ("GBR","GBR"),
    ("PL","PL"),
)

payment_type =(
    ("pay_by_link", "pay_by_link"),
    ("card", "card"),
    ("dp", "dp"),
)

class PayByLink(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(
        max_length=3,
        choices=currency_choices,
        default="1",
    )
    amount = models.IntegerField(validators=[MinValueValidator(10)])
    description = models.CharField(max_length=20)
    bank = models.CharField(max_length=5)

class DirectPayment(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(
        max_length=3,
        choices=currency_choices,
        default="1",
    )
    amount = models.IntegerField(validators=[MinValueValidator(10)])
    description = models.CharField(max_length=20)
    iban = models.CharField(max_length=30)

class Card(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(
        max_length=3,
        choices=currency_choices,
        default="1",
    )
    amount = models.IntegerField(validators=[MinValueValidator(10)])
    description = models.CharField(max_length=20)
    cartholder_name = models.CharField(max_length=30)
    cartholder_surname = models.CharField(max_length=30)
    cart_number = models.CharField(max_length=16)

class PaymentInfo(models.Model):
    date = models.DateTimeField()
    type = models.CharField(
        max_length=11,
        choices=payment_type,
        default="1",
    )
    payment_mean = models.CharField(max_length=30)
    description = models.CharField(max_length=20)
    amount = models.IntegerField(validators=[MinValueValidator(10)])
    currency = models.CharField(max_length=3)
    amount_in_pl = models.IntegerField(validators=[MinValueValidator(10)])

    def __str__(self):
        return self.type+' - '+self.payment_mean