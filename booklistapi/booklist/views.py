from django.shortcuts import render
from .models import Data
from .serializers import BookSerializers
from rest_framework import viewsets


class Booksviews(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = BookSerializers

# Create your views here.
