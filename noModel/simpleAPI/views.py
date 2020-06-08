from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import(
    permission_classes,
    authentication_classes,
    api_view
)
# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_temperature(request, format=None):
    return JsonResponse({
        "temp": 25,
        "Humidity": 45
    })
