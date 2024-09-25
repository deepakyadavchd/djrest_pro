from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import*


@api_view()
def helloview(request):
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def insertview(request):
    Car.objects.create(brandname="Ferrari", brandmodel="Roma", color="grey", milage="8 km/L", perdayrent="45000")
    return Response({"Insert": "You Added Successfully"})

@api_view(['GET'])
def carsview(request):
    crs=Car.objects.all().values()
    return Response({"car collections": crs})

@api_view(['GET'])
def filterview(request):
    fil=Car.objects.filter(brandname="Ford").values()
    return Response({"filter element": fil})

@api_view(['DELETE'])
def deleteview(request):
    Car.objects.filter(brandname="Maruti").delete()
    return Response({"delete": "filter element deleted successfully"})

