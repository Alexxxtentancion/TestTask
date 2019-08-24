from django.shortcuts import render
from .models import Person
# Create your views here.
from .serializers import PersonSerializer
from rest_framework import routers, serializers, viewsets





class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
