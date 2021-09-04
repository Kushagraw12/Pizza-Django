from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import pizza 
from . serializers import pizzaSerializer

# GET API
#1. Lists all pizzas in database
@api_view(['GET', ])
def api_all_pizza_view(request):
    try:
        p1 = pizza.objects.all()
    except pizza.DoesNotExist:
        return Response("NOT ALLOWED :: Database 'Pizza' does not exist", status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = pizzaSerializer(p1, many = True)
        return Response(ser.data, status = status.HTTP_200_OK) 


#2. Lists individual pizzas in databse, according to the requested SLUG
@api_view(['GET', ])
def api_indiv_pizza_view(request, slug):
    try:
        p1 = pizza.objects.get(slug = slug)
    except pizza.DoesNotExist:
        return Response("NOT ALLOWED :: Database 'Pizza' does not exist", status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = pizzaSerializer(p1)
        return Response(ser.data, status = status.HTTP_200_OK) 


#3. Lists all pizzas in databse, filtered according to the requested SIZE
@api_view(['GET', ])
def api_size_filter_pizza_view(request, size):
    try:
        p1 = pizza.objects.filter(size = size)
    except pizza.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = pizzaSerializer(p1, many = True)
        if(len(p1) == 0):
            return Response("FAIL :: No pizza of the given size exists", status = status.HTTP_404_NOT_FOUND)
        return Response(ser.data, status = status.HTTP_200_OK)
    return Response("FAIL :: No pizza of the given size exists", status = status.HTTP_404_NOT_FOUND)


#4. Lists all pizzas in databse, filtered according to the requested TYPE
@api_view(['GET', ])
def api_type_filter_pizza_view(request, type):
    try:
        p1 = pizza.objects.filter(type = type)
    except pizza.DoesNotExist:
        return Response("NOT ALLOWED :: Database Pizza does not exist", status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = pizzaSerializer(p1, many = True)
        if(len(p1) == 0):
            return Response("FAL :: No pizza of the given type exists", status = status.HTTP_404_NOT_FOUND)
        return Response(ser.data, status = status.HTTP_200_OK)
    return Response("FAIL :: No pizza of the given type exists", status = status.HTTP_404_NOT_FOUND)


#PUT API
#5. Edits a specific pizza based on the requested SLUG
@api_view(['PUT', ])
def api_update_pizza_view(request, slug):
    try:
        p1 = pizza.objects.get(slug = slug)
    except pizza.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        d = dict(request.data.lists())
        if "type" not in d:
            return Response("Not Updated :: Type Missing", status = status.HTTP_400_BAD_REQUEST)
        if "title" not in d:
            return Response("Not Updated :: Title Missing", status = status.HTTP_400_BAD_REQUEST)
        if "toppings" not in d:
            return Response("Not Updated :: Toppings Missing", status = status.HTTP_400_BAD_REQUEST)
        if "size" not in d:
            return Response("Not Updated :: Size Missing", status = status.HTTP_400_BAD_REQUEST)
        if d["type"][0] == 'Regular' or d["type"][0] == 'Square':
            ser = pizzaSerializer(p1, data = request.data)
            # data = {}

            if ser.is_valid():
                ser.save()
                # data["Success"] = "Update Succesful"
                return Response(data = ser.data, status = status.HTTP_200_OK)       
            return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(f"Not Updated ::  Pizza Type '{d['type'][0]}' not allowed", status = status.HTTP_400_BAD_REQUEST) 


#DELETE API
#6. Deletes a specific pizza from the database (Requires SLUG of that pizza)
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
            data["success"] = "Delete Succesfull"
        else:
            data["failure"] = "Delete Failed"
        return Response(data = data)


#POST API 
#7. Creates a Pizza in the Database
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
        return Response("Wrong Pizza Type", status = status.HTTP_400_BAD_REQUEST)