from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

GEEKS_CHOICES =(
    ("1", "EUR"),
    ("2", "USD"),
    ("3", "GBR"),
    ("4", "PL"),
)

class PayByLink(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(
        max_length=3,
        choices=GEEKS_CHOICES,
        default="1",
    )
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField()
    bank = models.CharField(max_length=5)

class DirectPayment(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(
        max_length=3,
        choices=GEEKS_CHOICES,
        default="1",
    )
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField()
    iban = models.CharField(max_length=30)

class Card(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(
        max_length=3,
        choices=GEEKS_CHOICES,
        default="1",
    )
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField()
    cartholder_name = models.CharField(max_length=30)
    cartholder_surname = models.CharField(max_length=30)
    cart_number = models.CharField(max_length=16)