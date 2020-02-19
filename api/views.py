import requests
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import ConvertCurrencySerializer
from django.conf import settings

URL = "https://currency.labstack.com/api/v1/convert/{}/USD/RUB"


class ConvertUSDToRUB(GenericAPIView):
    serializer_class = ConvertCurrencySerializer

    def post(self, request, *args, **kwargs):
        headers = {
            "Authorization": f"Bearer {settings.API_KEY}",
        }
        serializer = ConvertCurrencySerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.data.get('amount')
            response = requests.get(URL.format(amount), headers=headers)
            result = response.json()
            result['from'] = 'USD'
            result['to'] = 'RUB'
            return Response(result)
        return Response(serializer.error_messages)
