from rest_framework import serializers
from payment.models import PaymentInfo,PayByLink as PayByLinkModel


class PeymentInfoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = ['date','type','payment_mean','description','currency','amount','amount_in_pl']

class PayByLink(serializers.ModelSerializer):
    class Meta:
        model = PayByLinkModel
        fields = ['create_at','currency','amount','description','bank']

class PeymentInfoTypeSeralizer(serializers.Serializer):

    pay_by_link=serializers.SerializerMethodField()
    dp = serializers.SerializerMethodField()
    card = serializers.SerializerMethodField()

    def _build_payment_list(type_name):
        peyments = PaymentInfo.objects.all()
        serializer = PeymentInfoSeralizer(peyments, many=True)
        return serializer.data

    def get(self, obj):
        return self._build_payment_list(PaymentInfo.type)

    class Meta:
        fields = ['pay_by_link','dp','card']
