from rest_framework.serializers import Serializer, FloatField


class ConvertCurrencySerializer(Serializer):
    amount = FloatField(required=True)
