from django.urls import path
from .views import PropertyListView
from .views import seed_properties


urlpatterns = [
    path("properties/", PropertyListView.as_view(), name="property-list"),
    path("seed/", seed_properties),

]
