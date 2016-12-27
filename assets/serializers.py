from rest_framework.serializers import ModelSerializer


class DynamicModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        excludes = kwargs.pop('excludes', None)
        fields = kwargs.pop('fields', None)

        super(DynamicModelSerializer, self).__init__(*args, **kwargs)

        if excludes is not None:
            for field_name in set(self.fields.keys()).intersection(excludes):
                del self.fields[field_name]

        if fields is not None:
            for field_name in set(self.fields.keys()) - set(fields):
                del self.fields[field_name]
