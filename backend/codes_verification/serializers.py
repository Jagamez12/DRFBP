from rest_framework import serializers

from .models import Code

class CodeSerializer(serializers.Serializer):
    """ Serializador de los Code """
    class Meta:
        model = Code
        fields = ['email']
