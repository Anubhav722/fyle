from rest_framework.serializers import ModelSerializer
from bank.models import BankInfo


class BankInfoSerializer(ModelSerializer):

    class Meta:
        model = BankInfo
        fields = (
            "ifsc", "bank_id", "branch", "address", "city",
            "district", "state", "bank_name")
