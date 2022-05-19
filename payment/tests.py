from rest_framework.test import APITestCase
from django.urls import resolve
from django.urls import reverse
from rest_framework import status
from payment.views import PaymentInfoView, PayByLinkView, DirectPaymentView,CardView
from payment.models import PayByLink,DirectPayment,Card

class AbstratTest(APITestCase):
    many=True
    url_test=''

    def data_match(self):
        response = self.client.get(self.url_test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def view_match(self,view):
        self.assertEquals(resolve(self.url_test).func.view_class, view)

class PaymentInfo_test(AbstratTest):
    url_test = reverse("payment-info", kwargs={})

    def test_data_match(self):
        self.data_match()

    def test_view_math(self):
        self.view_match(PaymentInfoView)

class PayByLink_test(AbstratTest):
    url_test = reverse("pay-by-link", kwargs={})

    def test_data_match(self):
        self.data_match()

    def test_view_math(self):
        self.view_match(PayByLinkView)

    def test_add_pay_bay_link(self):
        data_post =  {
            "create_at": "2022-05-19T13:16:17.002683Z",
            "currency": "EUR",
            "amount": 1999,
            "description": "Gym"
        }
        self.assertEqual(PayByLink.objects.count(), 0)
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PayByLink.objects.count(), 1)
        self.assertEqual(PaymentInfoView.objects.count(), 1)

class DirectPayment_test(AbstratTest):
    url_test = reverse("direct-payment", kwargs={})

    def test_data_match(self):
        self.data_match()

    def test_view_math(self):
        self.view_match(DirectPaymentView)

    def test_add_dp_link(self):
        data_post =  {
            "create_at": "2022-05-19T13:28:38.737557Z",
            "currency": "EUR",
            "amount": 13333333,
            "description": "Fast Food",
            "iban": "13131313"
        }

        self.assertEqual(DirectPayment.objects.count(), 0)
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DirectPayment.objects.count(), 1)
        self.assertEqual(PaymentInfoView.objects.count(), 1)

class Card_test(AbstratTest):
    url_test = reverse("card", kwargs={})

    def test_data_match(self):
        self.data_match()

    def test_view_math(self):
        self.view_match(CardView)

    def test_add_dp_link(self):
        data_post =      {
            "create_at": "2022-05-19T11:10:26.666338Z",
            "currency": "EUR",
            "amount": 12,
            "description": "kotek już wpłacił",
            "cartholder_name": "John",
            "cartholder_surname": "Doe",
            "cart_number": "1234567812345678"
        },

        self.assertEqual(Card.objects.count(), 0)
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(PaymentInfoView.objects.count(), 1)

