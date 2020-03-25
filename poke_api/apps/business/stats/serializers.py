from rest_framework import serializers


class StatSerializer(serializers.Serializer):
    name = serializers.CharField()
