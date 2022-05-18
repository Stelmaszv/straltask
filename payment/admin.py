from django.contrib import admin
from .models import PayByLink,DirectPayment,Card
admin.site.register(PayByLink)
admin.site.register(DirectPayment)
admin.site.register(Card)