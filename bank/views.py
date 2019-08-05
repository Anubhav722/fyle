from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from bank.models import BankInfo
from bank.serializers import BankInfoSerializer


# Create your views here.


class BankDetails(ListAPIView):
    queryset = BankInfo.objects.all()
    serializer_class = BankInfoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = ("ifsc", "bank_id", "branch", "address", "city",
                     "district", "state", "bank_name")
    ordering_fields = ("ifsc",)
    ordering = ("ifsc",)
