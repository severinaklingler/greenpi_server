import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from .models import Measurement
from .serializers import MeasurementSerializer

# Create your views here.

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_measurement(request, format=None):
    serializer = MeasurementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def measurements(request, format=None):
    m = Measurement.objects.all()
    serializer = MeasurementSerializer(m, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def clean(request):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    m = Measurement.objects.filter(when__lt=yesterday).delete()
    return HttpResponse('OK.')