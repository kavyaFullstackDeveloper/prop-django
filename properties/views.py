from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from .models import Property
from .serializers import PropertySerializer

class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all().order_by("-dateListed")
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "location__city", "location__country"]
