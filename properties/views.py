from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from .models import Property
from .serializers import PropertySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from properties.models import Property
import random

class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all().order_by("-dateListed")
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "location__city", "location__country"]

@api_view(['POST', 'GET'])
def seed_properties(request):
    """Seed database with fresh demo property listings"""
    # 🚀 Clear existing data to avoid duplicates
    Property.objects.all().delete()

    cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Toronto']
    props = []

    for i in range(20):  # create 20 demo properties
        props.append(Property(
            name=f"Demo Property {i+1}",
            price=random.randint(100000, 800000),
            currency="USD",
            location={"city": random.choice(cities), "country": "USA"},
            area={"sqft": random.randint(500, 2500)},
            bedrooms=random.randint(1, 5),
            bathrooms=random.randint(1, 3),
            propertyType=random.choice(["Apartment", "House", "Villa"]),
            status=random.choice(["For Sale", "For Rent"]),
            rating=round(random.uniform(3.0, 5.0), 1),
            amenities=["Gym", "Pool", "Parking", "Garden"],
            agent={"name": f"Agent {i+1}", "phone": f"+123456789{i}"},
            images=[f"https://picsum.photos/400/300?random={i}"]
        ))

    Property.objects.bulk_create(props)  # 🚀 Fast insert

    return Response({"message": "20 fresh demo properties added ✅"})
