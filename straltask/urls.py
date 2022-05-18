"""straltask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from payment.views import PaymentInfoView, PaymentInfoByTypeView, PayByLinkView, DirectPaymentView, CardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment-info', PaymentInfoView.as_view(), name="payment-info"),
    path('payment-info-type', PaymentInfoByTypeView.as_view(), name="payment-info-type"),
    path('pay-by-link', PayByLinkView.as_view(), name="pay-by-link"),
    path('direct-payment', DirectPaymentView.as_view(), name="direct-payment"),
    path('card', CardView.as_view(), name="card"),
]
