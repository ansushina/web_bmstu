from rest_framework import serializers


class FilmQuerySerializer(serializers.Serializer):
    genre = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    country = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    actor = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    year_from = serializers.IntegerField(required=False)
    year_to = serializers.IntegerField(required=False)
    limit = serializers.IntegerField(required=False)
    sort = serializers.CharField(required=False)
    offset = serializers.IntegerField(required=False)
    q = serializers.CharField(required=False)
