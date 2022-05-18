from rest_framework import generics
from payment.models import PaymentInfo
from payment.seralisers import PeymentInfoSeralizer


class PaymentInfoView(generics.ListAPIView):

    Model = PaymentInfo
    queryset = PaymentInfo.objects.all()
    serializer_class = PeymentInfoSeralizer
