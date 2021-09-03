from rest_framework import serializers
from . models import pizza

class pizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = pizza 
        fields = '__all__'