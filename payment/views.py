import json
import os
from rest_framework import status
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

    def action_after_list(self,serializer,request):
        pass

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
        self.action_after_list(serializer,request)
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

class PaymentInfoId(PaymentInfoView):
    http_method_names = ['get']
    SerializerClass = PeymentInfoSeralizer

    def on_query_set(self, user):
        self.queryset = PaymentInfo.objects.filter(Customer=user)

class PaymentInfoSaveRaportId(PaymentInfoId):

    def on_query_set(self,user):
        self.queryset = PaymentInfo.objects.filter(Customer=user)

    def action_after_list(self,serializer,request):
        self.save_in_memory(serializer.data,request)

    def save_in_memory(self,data,request):
        json_str = json.dumps(data)
        loaction='raports/'+str(request.user.id)
        if os.path.isdir(loaction) is False:
            os.mkdir(loaction)
        if os.path.exists(loaction+'/raport.json'):
            os.remove(loaction+'/raport.json')
        a_file = open(loaction+'/raport.json', "w")
        json.dump(json.loads(json_str), a_file)
        a_file.close()


