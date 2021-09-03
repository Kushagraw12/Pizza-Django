from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import pizza 
from . serializers import pizzaSerializer

@api_view(['GET', ])
def api_all_pizza_view(request):
    try:
        p1 = pizza.objects.all()
    except pizza.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = pizzaSerializer(p1, many = True)
        return Response(ser.data) 

@api_view(['GET', ])
def api_indiv_pizza_view(request, slug):
    try:
        p1 = pizza.objects.get(slug = slug)
    except pizza.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = pizzaSerializer(p1)
        return Response(ser.data) 
    
@api_view(['PUT', ])
def api_update_pizza_view(request, slug):
    print("DATA: ", request.data)
    try:
        p1 = pizza.objects.get(slug = slug, data = request.data)
    except pizza.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        ser = pizzaSerializer(p1, data = request.data)
        data = {}

        if ser.is_valid():
            ser.save()
            data["success"] = "update succesful"
            return Response(data = data)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def api_delete_pizza_view(request, slug):
    try:
        p1 = pizza.objects.get(slug = slug)
    except pizza.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        operation = p1.delete() 
        data = {}
        if operation:
            data["success"] = "delete succesfull"
        else:
            data["failure"] = "delete failed"
        return Response(data = data)

@api_view(['POST', ])
def api_create_pizza_view(request):
    p1 = pizza()

    if request.method == "POST":
        d = dict(request.data.lists())
        if d["type"] == ['Regular'] or d["type"] == ['Square']:
            ser = pizzaSerializer(p1, data = request.data)
            data = {}
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status = status.HTTP_201_CREATED)
            return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response("Wrong Type", status = status.HTTP_400_BAD_REQUEST)