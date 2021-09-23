"""
Serialize models to JSON
"""
from rest_framework import serializers

from .models import Hero
from .models import Publisher
from .models import Superpower

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias')

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('name')

class SuperpowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Superpower
        fields = ('name')
