#from dataclasses import fields
from django.forms import ValidationError
from rest_framework import serializers

from teacher.models import Professor, Aula


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        #fields = ('id', 'nome', 'valor_hora', 'descricao', 'foto')


class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    nome = serializers.CharField(max_length=100)

#validação do nome
    def validate_nome(self, value):
        if len(value)<3:
            raise ValidationError("Nome deve ter mais que 3 letras")
            return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

