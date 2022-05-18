from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import PaymentInfo
from payment.seralisers import PeymentInfoSeralizer

class APIPrototype(APIView):
    reverse         = True
    SerializerClass = None
    many     = True
    queryset = ''
    order_by = ''
    http_method_names = ['get']

    def on_query_set(self):
        pass

    def list(self):
        self.on_query_set()
        serializer = self.SerializerClass(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(
                serializer.data,
                key=lambda tup: tup[self.order_by],
                reverse=self.reverse)
        else:
            list= serializer.data
        return list

    def api_get(self, request, *args, **kwargs):
        return Response(data=self.list(), status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.api_get(request)


class PaymentInfoView(APIPrototype):

    SerializerClass = PeymentInfoSeralizer
    queryset = PaymentInfo.objects
    reverse = True
    order_by = 'date'
