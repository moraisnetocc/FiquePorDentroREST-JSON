from rest_framework import viewsets

from api.serializers import InfoSerializer, Info, InfoCategorySerializer, InfoCategory


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoCategoryViewSet(viewsets.ModelViewSet):
    queryset = InfoCategory.objects.all()
    serializer_class = InfoCategorySerializer
