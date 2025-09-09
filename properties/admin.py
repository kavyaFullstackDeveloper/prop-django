from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "currency", "rating", "status")
    search_fields = ("name", "location")
