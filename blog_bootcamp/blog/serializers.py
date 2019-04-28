from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()