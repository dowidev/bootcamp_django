from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class NewsSerializer(serializers.Serializer):
    category = serializers.StringRelatedField()
    title = serializers.CharField()
    summary = serializers.CharField()
    content = serializers.CharField()
    image = serializers.ImageField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()