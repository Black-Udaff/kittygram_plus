from rest_framework import serializers

from .models import Cat, Owner


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year')


class OwnerSerializer(serializers.ModelSerializer):
    class meta:
        model = Owner
        Fields = ('first_name', 'last_name')
