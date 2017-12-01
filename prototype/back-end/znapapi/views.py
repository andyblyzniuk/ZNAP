from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from znapapi.models import Znap
from znapapi.serializers import ZnapSerialezer


class ZnapViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Znap.objects.all()
    serializer_class = ZnapSerialezer