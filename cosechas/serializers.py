from rest_framework import serializers
from .models import Cultivo, Cosecha

class CosechaSerializer(serializers.ModelSerializer):

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a 0 kg.")
        return value

    class Meta:
        model = Cosecha
        fields = "__all__"


class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = "__all__"
