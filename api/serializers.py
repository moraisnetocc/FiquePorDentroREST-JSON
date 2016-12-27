from rest_framework import serializers

from api.models import Info, InfoCategory
from assets.serializers import DynamicModelSerializer


class InfoSerializer(DynamicModelSerializer):
    class Meta:
        model = Info
        fields = ('title', 'body', 'category')


class InfoCategorySerializer(serializers.ModelSerializer):
    infos = InfoSerializer(many=True, read_only=True, excludes=['category'])

    class Meta:
        model = InfoCategory
        fields = ('name', 'infos')
