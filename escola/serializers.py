from rest_framework.serializers import ModelSerializer
from escola.models import Aluno, Professor, Turma

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        