from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Category, New
from blog.serializers import CategorySerializer, NewSerializer


@api_view(["GET"])
def hello_world(request):
    # PROCESSING DATA
    return Response({"message": "hello world"}) # RETURN DATA


@api_view(["GET"])
def categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)


@api_view(["GET"])
def get_category(request, pk):
    queryset = Category.objects.get(pk=pk)
    serialized = CategorySerializer(queryset)
    return Response(serialized.data)


@api_view(["GET"])
def news(request):
    queryset = New.objects.all()
    serialized = NewSerializer(queryset, many=True)
    return Response(serialized.data)


@api_view(["GET"])
def get_news(request, pk):
    queryset = New.objects.get(pk=pk)
    serialized = NewSerializer(queryset)
    return Response(serialized.data)