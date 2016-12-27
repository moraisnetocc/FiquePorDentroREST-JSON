from rest_framework import viewsets

from .models import Info
from .serializers import InfoSerializer

# Create your views here.


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
