from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class NewSerializer(serializers.Serializer):
    category = serializers.StringRelatedField()
    title = serializers.CharField()
    summary = serializers.CharField()
    content = serializers.CharField()
    image = serializers.ImageField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()