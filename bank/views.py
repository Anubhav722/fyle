from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend

from bank.models import BankInfo
from bank.serializers import BankInfoSerializer


# Create your views here.

@api_view(['GET'])
def get_bank_detail(request, ifsc):
    bank = get_object_or_404(BankInfo, ifsc=ifsc)
    ser = BankInfoSerializer(bank)
    return Response({"status": "success",
                     "details": ser.data},
                    status=status.HTTP_200_OK)


class BankDetails(ListAPIView):
    queryset = BankInfo.objects.all()
    serializer_class = BankInfoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = ("ifsc", "bank_id", "branch", "address", "city",
                     "district", "state", "bank_name")
    ordering_fields = ("ifsc",)
    ordering = ("ifsc",)
