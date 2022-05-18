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

def get_corent_var(var):
    return var

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

    def save(self, *args, **kwargs):
        super(PayByLink, self).save()
        PaymentInfo(
            date=str(self.create_at),
            type='pay_by_link',
            payment_mean='bank',
            description=self.description,
            currency=self.currency,
            amount=self.amount,
            amount_in_pl=get_corent_var(self.amount)
        ).save()

    def __str__(self):
        return self.description

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

    def save(self, *args, **kwargs):
        super(DirectPayment, self).save()
        PaymentInfo(
            date=str(self.create_at),
            type='db',
            payment_mean='iban',
            description=self.description,
            currency=self.currency,
            amount=self.amount,
            amount_in_pl=get_corent_var(self.amount)
        ).save()

    def __str__(self):
        return self.description

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

    def show_payment_mean(self):
        def hide(number):
            return 123

        return self.cartholder_name+' '+self.cartholder_surname+' '+str(hide(self.cart_number))

    def valid_card(self):
       try:
           int(self.cart_number)
       except:
           raise ValueError("Invalid Card Number !")

       if len(self.cart_number) != 16:
           raise ValueError("Invalid Card Number !")

    def save(self, *args, **kwargs):
        self.valid_card()
        super(Card, self).save()
        PaymentInfo(
            date=str(self.create_at),
            type='card',
            payment_mean=self.show_payment_mean(),
            description=self.description,
            currency=self.currency,
            amount=self.amount,
            amount_in_pl=get_corent_var(self.amount)
        ).save()

    def __str__(self):
        return self.show_payment_mean()

class PaymentInfo(models.Model):
    date = models.DateTimeField(null=False)
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