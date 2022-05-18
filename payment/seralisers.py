from rest_framework import serializers
from payment.models import PaymentInfo


class PeymentInfoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = ['date','type','payment_mean','description','currency','amount','amount_in_pl']