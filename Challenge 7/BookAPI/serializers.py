from BookAPI.models import BookData
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = BookData
        fields = ['id', 'name', 'category', 'description', 'rating', 'image']