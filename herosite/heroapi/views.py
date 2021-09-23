"""
views.py
"""
from rest_framework import viewsets

from .serializers import HeroSerializer, PublisherSerializer, SuperpowerSerializer
from .models import Hero, Publisher, Superpower



class HeroViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PublisherViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
<<<<<<< HEAD
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer

class SuperpowerViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = Superpower.objects.all().order_by('name')
    serializer_class = SuperpowerSerializer
=======
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class SuperpowerViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
>>>>>>> b2dcbbcca47ec775f4ee5551bc4950bd5864c1e6
