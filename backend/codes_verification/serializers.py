from rest_framework import serializers

from .models import Code

class CodeSerializer(serializers.ModelSerializer):
    """ Serializador de los Code """
    class Meta:
        model = Code
        fields = '__all__'
