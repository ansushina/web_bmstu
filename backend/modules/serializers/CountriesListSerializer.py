from rest_framework import serializers
from modules.serializers.GenreSerializer import GenreSerializer


class CountriesListSerializer(serializers.Serializer):
    countries = GenreSerializer(many=True, read_only=True)
