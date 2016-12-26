from rest_framework import serializers
from .models import Info



class InfoSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = Info
        fields = ('title','author')