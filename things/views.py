from django.shortcuts import render
from rest_framework import generics
from .models import Thing
from .serializers import ThingSerializers
# Create your views here.
class ThingList(generics.ListCreateAPIView):
    queryset=Thing.objects.all()
    serializer_class=ThingSerializers

class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset=Thing.objects.all()
   serializer_class=ThingSerializers