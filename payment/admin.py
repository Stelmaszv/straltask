from django.contrib import admin
from .models import PayByLink,DirectPayment
admin.site.register(PayByLink)
admin.site.register(DirectPayment)