from django.shortcuts import render
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Info
from .serializers import InfoSerializer

# Create your views here.


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

