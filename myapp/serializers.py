from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # This will include all fields from the Product model
        # read_only_fields = ['id']  # if you want to make the id field read-only