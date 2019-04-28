from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Category
from blog.serializers import CategorySerializer


@api_view(["GET"])
def hello_world(request):
    # PROCESSING DATA
    return Response({"message": "hello world"}) # RETURN DATA

@api_view(["GET"])
def categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)