from rest_framework import serializers
from .models import Vinilo, Cancion, Proveedor

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ViniloSerializer(serializers.ModelSerializer):
    canciones = CancionSerializer(many=True, read_only=True)

    class Meta:
        model = Vinilo
        fields = '__all__'
