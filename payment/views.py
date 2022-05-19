from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from payment.models import PaymentInfo,PayByLink,DirectPayment,Card
from payment.seralisers import PeymentInfoSeralizer, PeymentInfoTypeSeralizer,PayByLink as PayByLinkSeralizer,\
    DirectPayment as DirectPaymentSeralizer, Card as CardSeralizer

class APIPrototype(APIView):
    reverse         = True
    SerializerClass = None
    many     = True
    queryset = ''
    order_by = ''

    def on_query_set(self):
        pass

    def list(self,request):
        self.on_query_set(request.user)
        serializer = self.SerializerClass(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(
                serializer.data,
                key=lambda tup: tup[self.order_by],
                reverse=self.reverse)
        else:
            list= serializer.data
        return list

    def post(self, request, *args, **kwargs):
        serializer = self.SerializerClass(data=request.data, many=False)
        if serializer.is_valid():
            request.data['Customer']=request.user
            serializer.save()
            return Response(data=self.list(), status=status.HTTP_201_CREATED)
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        return Response(data=self.list(request), status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

class PaymentInfoView(APIPrototype):

    http_method_names = ['get']
    SerializerClass = PeymentInfoSeralizer
    queryset = PaymentInfo.objects
    reverse = True
    order_by = 'date'

class PaymentInfoId(PaymentInfoView):

    http_method_names = ['get']
    SerializerClass = PeymentInfoSeralizer

    def on_query_set(self,user):
        self.queryset = PaymentInfo.objects.filter(Customer=user)

class PaymentInfoByTypeView(APIPrototype):

    http_method_names = ['get']
    SerializerClass = PeymentInfoTypeSeralizer
    queryset = PaymentInfo.objects

class PayByLinkView(APIPrototype):

    serializer_class = PayByLinkSeralizer
    queryset = PayByLink.objects

class DirectPaymentView(APIPrototype):

    serializer_class = DirectPaymentSeralizer
    queryset = DirectPayment.objects

class CardView(APIPrototype):

    SerializerClass = CardSeralizer
    queryset = Card.objects


