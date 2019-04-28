from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Category, News
from blog.serializers import CategorySerializer, NewsSerializer


@api_view(["GET"])
# test hello world before move on
def hello_world(request):
  return Response({"message" : "hello world"})

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
    queryset = News.objects.all()
    serialized = NewsSerializer(queryset, many=True)
    return Response(serialized.data)

@api_view(["GET"])
def get_news(request, pk):
    queryset = News.objects.get(pk=pk)
    serialized = NewsSerializer(queryset)
    return Response(serialized.data)