from rest_framework import serializers
from . models import pizza

class pizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = pizza 
        # Currently showing all the fileds in Pizza
        fields = '__all__'
        # Comment the above line & Uncomment the following line to hide id and slug
        # fields = ['title', 'type', 'size', 'toppings']