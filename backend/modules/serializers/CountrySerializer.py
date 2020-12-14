from rest_framework import serializers


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)


