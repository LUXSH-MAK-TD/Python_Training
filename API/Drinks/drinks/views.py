from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserlializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 


@api_view(['GET','POST',])
    
def drinklist(request):
   
 if request.method == 'GET':
    drinks = Drink.objects.all()
    serializer = Drinkserlializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data})
 
 if request.method == 'POST':
    serializer = Drinkserlializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(id=id)
    except Drink.DoesNotExist:
        return JsonResponse({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Drinkserlializer(drink)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = Drinkserlializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    